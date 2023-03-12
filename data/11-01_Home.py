import streamlit as st

st.set_page_config(page_title="shopee.vn", page_icon=":moneybag:")
st.title("Sentiment Analysis")

# st.markdown("# Main page")
st.sidebar.markdown("# Business Objective")

st.subheader("Sentiment Analysis trong E-commerce")
st.write("""
* Ngày nay, nhu cầu mua sắm online ngày càng
cao. Không cần phải đi xa, chúng ta có thể lên
các trang thương mại điện tử để đặt mua mọi
thứ.
""")  
st.write("""* Để lựa chọn một sản phẩm chúng ta có xu
hướng xem xét những bình luận từ những
người đã mua/ trải nghiệm để đưa ra quyết
định có nên mua hay không?.""")
st.write("""* Những phản hồi của khách hàng rất quan
trọng, từ đó có thể giúp cho nhà cung cấp
cải thiện chất lượng của hàng hóa/ dịch vụ
cũng như thái độ phục vụ nhằm duy trì uy
tín của nhà cung cấp cũng như tìm kiếm
thêm khách hàng mới.
""")
st.write("""* => Xây dựng hệ thống hỗ trợ phân loại các
phản hồi của khách hàng thành các nhóm:
tích cực, tiêu cực, trung tính dựa trên dữ liệu
dạng văn bản.""")
st.image("images/what-is-sentiment-analysis.jpg")
st.subheader("Mục tiêu dự án")
st.image("images/shopee-1.jpg")
st.write("""* Shopee là một hệ sinh thái
thương mại “all in one”,
trong đó có shopee.vn, là
một website thương mại
điện tử đứng top 1 của Việt
Nam và khu vực Đông
Nam Á.""")
st.write("""* Chúng ta có thể lên đây để xem thông tin sản
phẩm, đánh giá, nhận xét cũng như đặt mua.
            """)
st.write("""* Mục tiêu/ vấn đề: Xây dựng mô hình dự đoán giúp
người bán hàng có thể biết được những phản hồi nhanh
chóng của khách hàng về sản phẩm hay dịch vụ của họ
(tích cực hay tiêu cực), điều này giúp cho người
bán biết được tình hình kinh doanh, hiểu được ý kiến của
khách hàng từ đó giúp họ cải thiện hơn trong dịch vụ, sản
phẩm.""")