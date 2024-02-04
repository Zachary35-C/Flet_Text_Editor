import flet as ft

def main(page: ft.page):
    page.title = "Text Editor"
    page.theme_mode = ft.ThemeMode.DARK
    page.scrollbar = any
    appbar_text_ref = ft.Ref[ft.Text]()
    page.update()
    
    #Pick files dialog
    
    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        selected_files.update()
        
    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()
    
    #Save file dialog
    
    def save_file_result(e: ft.FilePickerResultEvent):
        save_file_path.value = e.path if e.path else "Cancelled!"
        save_file_path.update()
        
    save_file_dialog = ft.FilePicker(on_result=save_file_result)
    save_file_path = ft.Text()
    
    #Open directory dialog
    
    def get_directory_result(e: ft.FilePickerResultEvent):
        directory_path.value = e.path if e.path else "Cancelled"
        directory_path.update()
        page.update()
    
    get_directory_dialog = ft.FilePicker(on_result=get_directory_result)
    directory_path = ft.Text()
    
    page.overlay.extend([pick_files_dialog, save_file_dialog, get_directory_dialog])
    

    ft.page.appbar = ft.AppBar(
        title=ft.Text("Menus", ref=appbar_text_ref),
        center_title=True,
        bgcolor=ft.colors.BLUE 
    )  
    
    menubar = ft.MenuBar(
        expand=True,
        style=ft.MenuStyle(
            alignment=ft.alignment.top_left,
            bgcolor=ft.colors.BLUE,
            mouse_cursor={ft.MaterialState.HOVERED: ft.MouseCursor.WAIT,
                          ft.MaterialState.DEFAULT: ft.MouseCursor.ZOOM_OUT},
            ),
        controls=[
            ft.SubmenuButton(
                content=ft.Text("File"),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Open"),
                        leading=ft.Icon(ft.icons.FILE_OPEN),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.PURPLE}),
                        on_click=lambda _: get_directory_dialog.get_directory_path(),
                        disabled=page.web,                       
                     ),
                    directory_path,
                    
                    ft.MenuItemButton(
                        content=ft.Text("Saved"),
                        leading=ft.Icon(ft.icons.SAVE),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.PURPLE}),
                        on_click=lambda _: save_file_dialog.save_file(),
                        disabled=page.web,
                    ),
                    save_file_path,
                    
                    ft.MenuItemButton(
                        content=ft.Text("Quit"),
                        leading=ft.Icon(ft.icons.CLOSE),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.PURPLE}),
                        on_click=lambda _: exit()
                    )
                ]
            ),
            ft.SubmenuButton(
                content=ft.Text("Value"),
                controls=[
                    ft.SubmenuButton(
                        content=ft.Text("Zoom"),
                        controls=[
                            ft.MenuItemButton(
                                content=ft.Text("Magniy"),
                                leading=ft.Icon(ft.icons.ZOOM_IN),
                                close_on_click=False,
                                style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.PURPLE}),
                                
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Magniy"),
                                leading=ft.Icon(ft.icons.ZOOM_OUT),
                                close_on_click=False,
                                style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.PURPLE}),
                                
                            ),
                        ]
                    )
                ]         
            )
        ]
    )
    
    text_field = ft.TextField(
        value="",
        multiline=True,
        expand=True,
        border_color=ft.colors.TRANSPARENT,
        
    )
    
    page.add(
        ft.Row([menubar]),
        text_field,
    ) 


ft.app(target=main)