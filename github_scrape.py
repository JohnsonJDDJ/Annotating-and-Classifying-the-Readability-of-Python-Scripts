"""
Things to note:
1): This crawler uses the clipboard, so don't copy stuff while this running, otherwise it will overwrite contents in the clipboard
2): Don't minimize the window, otherwise selenium doesn't work correctly
3): Github returns at most 1000 files, 10 files each page for 100 pages even though there can be millions of files that are avaible,
Thus refreshing the page returns different files 

====================================
SETUP: Plese Define Global Variables
"""
USER = "JD" # identify urself
HASH_PATH = "./" + USER + "_hash.pkl" # store data hashes; defaults to ./hash.pkl
DATA_PATH = "./raw_data/" # place to store data; defaults to ./data/
GITHUB_USER = "JohnsonJDDJ" # github username
"""
====================================
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import time, os 
import clipboard
import pickle

# Read Github Password from ./GITHUB_PASSWORD
# You must have this file
GITHUB_PASSWORD = None
with open("./GITHUB_PASSWORD", "r") as f:
    GITHUB_PASSWORD = str(f.read())
if GITHUB_PASSWORD is None:
    raise AssertionError("Missing password in ./GITHUB_PASSWORD")
print(GITHUB_PASSWORD)

hashes = set()
if os.path.exists(HASH_PATH):
    with open(HASH_PATH,"rb") as f:
        hashes = pickle.load(f)

def save_file(index, filename):
    content = clipboard.paste()
    if hash(content) in hashes:
        return False
    hashes.add(hash(content))
    #only choose the filename
    filename = filename.split("/")[-1]
    filename = "{}{}-{}".format(USER, index, filename)
    file_path = os.path.join(DATA_PATH, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    return True

try:
    #if anything irrecoverable happens here, save the hashed file so we can restart
    service = Service(executable_path="./chromedriver")
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--enable-features=NetworkService')
    driver = webdriver.Chrome(service=service)
    driver.get("https://github.com/search?q=extension%3Apy+size%3A1800..2200&type=Code")

    #this will initiate a login process 
    wait = WebDriverWait(driver, 6)
    wait.until(EC.presence_of_element_located((By.ID, "login_field")))
    wait.until(EC.presence_of_element_located((By.ID, "password")))
    wait.until(EC.element_to_be_clickable((By.NAME, "commit")))
    driver.find_element(By.ID, "login_field").send_keys(GITHUB_USER)
    driver.find_element(By.ID, "password").send_keys(GITHUB_PASSWORD) # change this to your github password
    driver.find_element(By.NAME, "commit").click()
    time.sleep(3)

    # at this point we should arrive at the page where each file is being listed
    while len(hashes) < 800:
        print("scraped: {}".format(len(hashes)))

        while True:
            try:
                wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "f4")))
                lst = driver.find_elements(By.CLASS_NAME, "f4")
                if len(lst) < 10:
                    raise RuntimeError
                else:
                    break
            except:
                #there can be some problems loading the page, so try to refresh it a couple of times
                driver.refresh()

        time.sleep(2.5)

        files = [i.find_element(By.XPATH,".//a").text for i in lst]
        for file in files:
            wait.until(EC.presence_of_element_located((By.LINK_TEXT,file)))
            element = driver.find_element(By.LINK_TEXT,file)
            wait.until(EC.element_to_be_clickable(element))
            element.click()
            time.sleep(1)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".d-inline-block.btn-octicon")))
            element = driver.find_element(By.CSS_SELECTOR,".d-inline-block.btn-octicon")
            wait.until(EC.element_to_be_clickable(element))
            element.click()
            #sleep for 1 second after clicking so there is always time to process
            #and so this shit doesn't crash 
            time.sleep(0.5)
            #save the file here
            val = save_file(len(hashes), file)
            driver.back()
            time.sleep(1)

        #hopefully by this point every file on this page has been stored 
        #we go to the next page
        next_page = driver.find_element(By.CSS_SELECTOR,"a[rel='next']")
        wait.until(EC.element_to_be_clickable(next_page))
        next_page.click()

        #sleep here so it doesn't loop on the same page
        time.sleep(3)

except Exception as e:
    print(e)
    with open(HASH_PATH,"wb") as f:
        #overwrite the old one is fine since we are starting off with what was there 
        pickle.dump(hashes,f)


