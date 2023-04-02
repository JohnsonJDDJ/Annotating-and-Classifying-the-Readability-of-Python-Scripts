from environs import Env

from api import MentorsAPI


def main() -> None:
    env = Env()
    env.read_env()

    mentors_api = MentorsAPI(env.str('DVMN_USERNAME'), env.str('DVMN_PASSWORD'))
    mentor_uuid = env.str('MENTOR_UUID')

    orders = mentors_api.get_mentor_orders(mentor_uuid)

    for order in orders:
        if not order['is_active']:
            continue

        notes = order['student']['notes']
        proj_notes = [
            n for n in notes if 
            'На проекте' in n['content']
            and not n['is_hidden']
        ]
        if not proj_notes:
            continue

        tasks = mentors_api.get_study_program_by_order_uuid(order['uuid'])
        project_task = None
        for task in tasks:
            if any([
                'Командные проекты' not in task['trainer']['title'],
                task['is_completed']
            ]):
                continue

            project_task = task
            break
        
        if not project_task:
            print(f'Ученику: {order["uuid"]} не выдан командный проект.')
            continue
        
        try:
            plan_uuid = mentors_api.create_weekly_plan(
                order['uuid'],
                project_task['uuid'],
                project_task['execution_time']
            )
            mentors_api.create_gist(plan_uuid)
            mentors_api.give_weekly_plan(
                order['uuid'],
                project_task['uuid'],
                project_task['execution_time'],
                plan_uuid
            )
            mentors_api.update_gist(plan_uuid)
        except Exception as err:
            print(f'Что-то пошло не так в заказе: {order["uuid"]}')
        else:
            for n in proj_notes:
                mentors_api.close_note(n['uuid'])

            mentors_api.add_note(
                student_uuid=order['student']['profile']['uuid'],
                comment='$: Настала пора командных проектов! Как настрой?)'
            )



if __name__ == '__main__':
    main()