import flet as ft

def main(page: ft.Page):
    def page_resize(e):
        res.height = page.height-70
        page.update()

    page.on_resize = page_resize
    main = ft.Column(controls=[
        ft.IconButton(icon=ft.icons.DOMAIN_VERIFICATION),
        ft.Container(content=ft.IconButton(icon=ft.icons.DASHBOARD)),
    ],alignment=ft.MainAxisAlignment.START,)
    additions = ft.Column(controls=[
        ft.IconButton(icon=ft.icons.MENU),
    ],alignment=ft.MainAxisAlignment.END)
    res = ft.Column(controls=[main, additions],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                horizontal_alignment=ft.MainAxisAlignment.START)
    page.add(res)
    page_resize(None)

ft.app(target=main)