import flet as ft
from moviepy.editor import VideoFileClip

def main(page: ft.Page):
    page.title = "Conversor de Vídeo"
    page.window.width = 420
    page.window.height = 780
    page.window.resizable = False
    page.window.maximizable = False
    page.window.always_on_top = True
    page.theme_mode = ft.ThemeMode.LIGHT


    def radiogroup_changed(e):
        pass

    
    texto_escolha_o_formato = ft.Text(
        value="Escolha o formato:",
        weight="bold",
        size=18,
        color="#FFC312",
    )
    
    extensao_radios = ft.RadioGroup(content=ft.Row([
            ft.Radio(
                value="mp4", label=".mp4",
                adaptive=True, active_color="#FFC312",
                label_style=ft.TextStyle(color="#FFC312"),
                fill_color={
                    ft.ControlState.HOVERED: "#FFC312",
                }
            ),
            ft.Radio(
                value="avi", label=".avi",
                adaptive=True, active_color="#FFC312",
                label_style=ft.TextStyle(color="#FFC312"),
                fill_color={
                    ft.ControlState.HOVERED: "#FFC312",
                }
            ),
            ft.Radio(
                value="mov", label=".mov",
                adaptive=True, active_color="#FFC312",
                label_style=ft.TextStyle(color="#FFC312"),
                fill_color={
                    ft.ControlState.HOVERED: "#FFC312",
                }
            ),
        ]),
        value="mp4",
        on_change=radiogroup_changed
    )

    def on_dialog_result(e: ft.FilePickerResultEvent):
        if not e.files:
            return
        
        selected = e.files[0].path
        source.value = f"Arquivo selecionado: {selected}"
        page.update()


    def convert_video(e):

        if not source.value:
            result.value = "Por favor, escolha um arquivo de vídeo."
            page.update()
            return
        
        result.value = ""
        page.update()
        
        
        try:
            sourceFile = source.value
            formato_do_arquivo = extensao_radios.value

            sourceFileSplitted = sourceFile.split(".")
            sourceFilePath = sourceFileSplitted[0]
            currentExtension = sourceFileSplitted[-1]

            caminho_original = source.value.split(":")[2]
            print(caminho_original)
            if currentExtension == formato_do_arquivo:
                result.value = "A extensão é a mesma do arquivo selecionado"
                page.update()
                return
            
            progressbar.visible = True
            page.update()

            caminho_convertido = caminho_original.replace(f".{currentExtension}", f".{formato_do_arquivo}")
            print(caminho_convertido)
            
        
            clip = VideoFileClip(caminho_original)
            clip.write_videofile(caminho_convertido, codec="libx264", audio_codec="aac")
            clip.close()

            result.value = f"Conversão concluída: {caminho_convertido}"

        except Exception as ex:
            result.value = f"Erro ao converter o vídeo: {ex}"

        progressbar.visible = False
        page.update()



    source = ft.Text(
        value="",
        size=16,
        color="#55EfC4",
        weight="light",
        opacity=0.5,
        max_lines=4,
        width=300,
    )

    result = ft.Text(
        value="",
        size=16,
        color="#55EfC4",
        weight="light",
        opacity=0.5,
        max_lines=4,
        width=300,
    )



    file_picker = ft.FilePicker(on_result=on_dialog_result)
    page.overlay.append(file_picker)

    progressbar = ft.ProgressBar(width=300, color="#FFC312", visible=False)

    btn_file_picker = ft.ElevatedButton(
        width=260,
        height=50,
        bgcolor="#262626",
        content=ft.Text(
            "Escolher o arquivo de vídeo...",
            weight=ft.FontWeight.BOLD,
            color="#18F88E",
        ),
        on_click=lambda _: file_picker.pick_files(allow_multiple=False)
    )

    btn_convert = ft.ElevatedButton(
        width=260,
        height=50,
        bgcolor="#262626",
        content=ft.Text(
            "Converter vídeo",
            weight=ft.FontWeight.BOLD,
            color="#18F88E",
        ),
        on_click=convert_video
    )

    page.add(
        ft.Container(
            width=400,
            height=720,
            bgcolor="#000000",
            border_radius=35,
            padding=ft.padding.only(left=20, top=60, right=20),

            content=ft.Column(
                spacing=20,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                value="CONVERSOR DE \n VÍDEO ✌️",
                                size=30,
                                color="#1BF88E",
                                weight="bold"
                            ),
                        ]
                    ),
                    ft.Column(),ft.Column(),
                    ft.Row(alignment=ft.MainAxisAlignment.CENTER,
                           controls=[btn_file_picker]),
                    ft.Column(
                        spacing=10,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Row(
                                spacing=0,
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    source
                                ]
                            )
                        ]
                    ),
                    ft.Row(), ft.Row(),
                    ft.Row(alignment=ft.MainAxisAlignment.CENTER,
                           controls=[texto_escolha_o_formato]),
                    ft.Row(
                        spacing=0,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[extensao_radios]),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[btn_convert]),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[result]),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[progressbar]),
                ]
            ),
        )
    )

ft.app(target=main)