import flet as ft
from login import *
# GUI模块


def update_text(dict_obj: dict):
    return ft.Row(
        [
            ft.Text(value=dict_obj['course_name'], size=20,),
            ft.Text(value=dict_obj['title'], size=20),
            ft.Text(value=dict_obj['end_time'], size=20)
        ], alignment=ft.MainAxisAlignment.CENTER
    )


def main(page: ft.Page):
    cookies = read_headers()['Cookie']
    cookies_in_field = ft.Ref[ft.TextField]()
    total_text = ft.Column()

    def search_clicked(e):
        # TODO：忧化逻辑
        headers = read_headers()
        headers['Cookie'] = cookies_in_field.current.value
        write_headers(headers)
        todo_list = login()
        items = []
        for i in todo_list:
            items.append(update_text(i))
        page.add(ft.Column(items))
        page.update()

    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    page.title = '作业快速查询工具'
    page.add(ft.Row([
        ft.TextField(ref=cookies_in_field, width=500, label='Cookies',
                     autofocus=True),
        ft.ElevatedButton(text='查询', on_click=search_clicked),
        ft.Column(ref=total_text)
    ], alignment=ft.MainAxisAlignment.CENTER)
    )
    if cookies != '':
        cookies_in_field.current.value = str(cookies)
    page.update()
