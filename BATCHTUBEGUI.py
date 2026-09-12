import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import subprocess
import threading
import os
import sys

def resource_path(relative_path):
    """ PyInstaller ile oluşturulan .exe dosyasının içindeki geçici klasör yolunu bulur. """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# --- Dil ve Tema Seçenekleri ---
LANGS = {
    "English": {
        "title": "BatchTube V2 (GUI by ROGER)",
        "dest": "Save Folder:",
        "browse": "Browse",
        "browser": "Browser (Cookies):",
        "url": "YouTube Link:",
        "btn_vid": "Download Video (MP4)",
        "btn_aud": "Download Audio (MP3)",
        "btn_upd": "Update yt-dlp",
        "log": "Process Log:",
        "no_cookie": "No Cookies",
        "theme": "Theme:",
        "light": "Light",
        "dark": "Dark",
        "err_link": "Please enter a valid YouTube link!",
        "err_dest": "Please select a save folder!",
        "err_exe": "yt-dlp.exe not found in the script folder!",
        "done": "[SUCCESS] Process completed!",
        "about": "About",
        "about_text": "BatchTube V2\nDeveloper: ROGER\nA graphical interface for yt-dlp."
    },
    "Türkçe": {
        "title": "BatchTube V2 (GUI by ROGER)",
        "dest": "Kayıt Klasörü:",
        "browse": "Seç",
        "browser": "Tarayıcı (Çerezler):",
        "url": "YouTube Linki:",
        "btn_vid": "Video İndir (MP4)",
        "btn_aud": "Ses İndir (MP3)",
        "btn_upd": "yt-dlp Güncelle",
        "log": "İşlem Kayıtları:",
        "no_cookie": "Çerezsiz",
        "theme": "Tema:",
        "light": "Açık",
        "dark": "Koyu",
        "err_link": "Lütfen geçerli bir YouTube linki girin!",
        "err_dest": "Lütfen bir kayıt klasörü seçin!",
        "err_exe": "yt-dlp.exe aynı klasörde bulunamadı!",
        "done": "[BAŞARILI] İşlem tamamlandı!",
        "about": "Hakkında",
        "about_text": "BatchTube V2\nGeliştirici: ROGER\nyt-dlp için gelişmiş grafik arayüzü."
    },
    "Azərbaycan": {
        "title": "BatchTube V2 (GUI by ROGER)",
        "dest": "Yaddaş Qovluğu:",
        "browse": "Seç",
        "browser": "Brauzer (Kukilər):",
        "url": "YouTube Linki:",
        "btn_vid": "Video Yüklə (MP4)",
        "btn_aud": "Səs Yüklə (MP3)",
        "btn_upd": "yt-dlp Yenilə",
        "log": "Əməliyyat Qeydləri:",
        "no_cookie": "Kukisiz",
        "theme": "Mövzu:",
        "light": "Açıq",
        "dark": "Tünd",
        "err_link": "Zəhmət olmasa düzgün YouTube linki daxil edin!",
        "err_dest": "Zəhmət olmasa yaddaş qovluğunu seçin!",
        "err_exe": "yt-dlp.exe eyni qovluqda tapılmadı!",
        "done": "[UĞURLU] Əməliyyat tamamlandı!",
        "about": "Haqqında",
        "about_text": "BatchTube V2\nTərtibatçı: ROGER\nyt-dlp üçün qrafik interfeys."
    },
    "Русский": {
        "title": "BatchTube V2 (GUI by ROGER)",
        "dest": "Папка сохранения:",
        "browse": "Обзор",
        "browser": "Браузер (Cookies):",
        "url": "Ссылка YouTube:",
        "btn_vid": "Скачать видео (MP4)",
        "btn_aud": "Скачать аудио (MP3)",
        "btn_upd": "Обновить yt-dlp",
        "log": "Журнал:",
        "no_cookie": "Без Cookies",
        "theme": "Тема:",
        "light": "Светлая",
        "dark": "Темная",
        "err_link": "Пожалуйста, введите правильную ссылку YouTube!",
        "err_dest": "Пожалуйста, выберите папку для сохранения!",
        "err_exe": "yt-dlp.exe не найден в папке!",
        "done": "[УСПЕШНО] Процесс завершен!",
        "about": "О программе",
        "about_text": "BatchTube V2\nРазработчик: ROGER\nГрафический интерфейс для yt-dlp."
    },
    "Português": {
        "title": "BatchTube V2 (GUI by ROGER)",
        "dest": "Pasta de Destino:",
        "browse": "Procurar",
        "browser": "Navegador (Cookies):",
        "url": "Link do YouTube:",
        "btn_vid": "Baixar Vídeo (MP4)",
        "btn_aud": "Baixar Áudio (MP3)",
        "btn_upd": "Atualizar yt-dlp",
        "log": "Registro:",
        "no_cookie": "Sem Cookies",
        "theme": "Tema:",
        "light": "Claro",
        "dark": "Escuro",
        "err_link": "Por favor, insira um link válido do YouTube!",
        "err_dest": "Por favor, selecione uma pasta de destino!",
        "err_exe": "yt-dlp.exe não encontrado na pasta!",
        "done": "[SUCESSO] Processo concluído!",
        "about": "Sobre",
        "about_text": "BatchTube V2\nDesenvolvedor: ROGER\nInterface gráfica para yt-dlp."
    },
    "Français": {
        "title": "BatchTube V2 (GUI by ROGER)",
        "dest": "Dossier de dest:",
        "browse": "Parcourir",
        "browser": "Navigateur (Cookies):",
        "url": "Lien YouTube:",
        "btn_vid": "Télécharger Vidéo (MP4)",
        "btn_aud": "Télécharger Audio (MP3)",
        "btn_upd": "Mettre à jour yt-dlp",
        "log": "Journal:",
        "no_cookie": "Sans Cookies",
        "theme": "Thème:",
        "light": "Clair",
        "dark": "Sombre",
        "err_link": "Veuillez entrer un lien YouTube valide!",
        "err_dest": "Veuillez sélectionner un dossier!",
        "err_exe": "yt-dlp.exe introuvable dans le dossier!",
        "done": "[SUCCÈS] Processus terminé!",
        "about": "À propos",
        "about_text": "BatchTube V2\nDéveloppeur: ROGER\nInterface graphique pour yt-dlp."
    },
    "Español": {
        "title": "BatchTube V2 (GUI by ROGER)",
        "dest": "Carpeta destino:",
        "browse": "Explorar",
        "browser": "Navegador (Cookies):",
        "url": "Enlace de YouTube:",
        "btn_vid": "Descargar Video (MP4)",
        "btn_aud": "Descargar Audio (MP3)",
        "btn_upd": "Actualizar yt-dlp",
        "log": "Registro:",
        "no_cookie": "Sin Cookies",
        "theme": "Tema:",
        "light": "Claro",
        "dark": "Oscuro",
        "err_link": "¡Ingrese un enlace válido de YouTube!",
        "err_dest": "¡Seleccione una carpeta de destino!",
        "err_exe": "¡yt-dlp.exe no se encontró en la carpeta!",
        "done": "[ÉXITO] ¡Proceso completado!",
        "about": "Acerca de",
        "about_text": "BatchTube V2\nDesarrollador: ROGER\nInterfaz gráfica para yt-dlp."
    },
    "中文": {
        "title": "BatchTube V2 (GUI by ROGER)",
        "dest": "保存文件夹:",
        "browse": "浏览",
        "browser": "浏览器 (Cookies):",
        "url": "YouTube 链接:",
        "btn_vid": "下载视频 (MP4)",
        "btn_aud": "下载音频 (MP3)",
        "btn_upd": "更新 yt-dlp",
        "log": "日志:",
        "no_cookie": "无 Cookies",
        "theme": "主题:",
        "light": "浅色",
        "dark": "深色",
        "err_link": "请输入有效的 YouTube 链接！",
        "err_dest": "请选择保存文件夹！",
        "err_exe": "文件夹中未找到 yt-dlp.exe！",
        "done": "[成功] 进程完成！",
        "about": "关于",
        "about_text": "BatchTube V2\n开发者: ROGER\nyt-dlp 的图形界面。"
    },
    "日本語": {
        "title": "BatchTube V2 (GUI by ROGER)",
        "dest": "保存先フォルダ:",
        "browse": "参照",
        "browser": "ブラウザ (Cookies):",
        "url": "YouTube リンク:",
        "btn_vid": "動画をDL (MP4)",
        "btn_aud": "音声をDL (MP3)",
        "btn_upd": "yt-dlp を更新",
        "log": "ログ:",
        "no_cookie": "Cookieなし",
        "theme": "テーマ:",
        "light": "ライト",
        "dark": "ダーク",
        "err_link": "有効なYouTubeリンクを入力してください！",
        "err_dest": "保存先フォルダを選択してください！",
        "err_exe": "フォルダに yt-dlp.exe が見つかりません！",
        "done": "[成功] 処理が完了しました！",
        "about": "情報",
        "about_text": "BatchTube V2\n開発者: ROGER\nyt-dlp 用のグラフィカルインターフェース。"
    }
}

class YTDLApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.current_lang = "Türkçe"
        self.is_dark_mode = True
        self.t = LANGS[self.current_lang]
        
        self.title(self.t["title"])
        self.geometry("700x550")
        self.minsize(650, 500) 
        self.resizable(True, True) 
        
        try:
            icon_file = resource_path("icon.ico")
            self.iconbitmap(icon_file)
        except Exception:
            pass 
        
        self.create_widgets()
        self.update_texts()
        self.apply_theme()

    def create_widgets(self):
        self.top_frame = tk.Frame(self)
        self.top_frame.pack(pady=10, fill="x", padx=10)

        self.lbl_lang = tk.Label(self.top_frame, text="Language / Dil:")
        self.lbl_lang.pack(side=tk.LEFT, padx=5)
        self.cb_lang = ttk.Combobox(self.top_frame, values=list(LANGS.keys()), state="readonly", width=12)
        self.cb_lang.set(self.current_lang)
        self.cb_lang.pack(side=tk.LEFT)
        self.cb_lang.bind("<<ComboboxSelected>>", self.change_lang)

        self.lbl_theme = tk.Label(self.top_frame, text=self.t["theme"])
        self.lbl_theme.pack(side=tk.LEFT, padx=(15, 5))
        self.cb_theme = ttk.Combobox(self.top_frame, state="readonly", width=10)
        self.cb_theme.pack(side=tk.LEFT)
        self.cb_theme.bind("<<ComboboxSelected>>", self.change_theme)

        # HAKKINDA BUTONU
        self.btn_about = tk.Button(self.top_frame, text=self.t["about"], command=self.show_about, relief=tk.GROOVE)
        self.btn_about.pack(side=tk.RIGHT, padx=5)

        self.form_frame = tk.Frame(self)
        self.form_frame.pack(pady=10, padx=20, fill="x")
        self.form_frame.columnconfigure(1, weight=1) 

        self.lbl_dest = tk.Label(self.form_frame, text=self.t["dest"], width=18, anchor="w")
        self.lbl_dest.grid(row=0, column=0, pady=5, sticky="w")
        self.ent_dest = tk.Entry(self.form_frame)
        self.ent_dest.grid(row=0, column=1, pady=5, sticky="ew")
        self.btn_browse = tk.Button(self.form_frame, text=self.t["browse"], command=self.browse_folder)
        self.btn_browse.grid(row=0, column=2, padx=10)

        self.lbl_browser = tk.Label(self.form_frame, text=self.t["browser"], width=18, anchor="w")
        self.lbl_browser.grid(row=1, column=0, pady=5, sticky="w")
        self.browsers = [self.t["no_cookie"], "chrome", "edge", "firefox", "brave", "opera"]
        self.cb_browser = ttk.Combobox(self.form_frame, values=self.browsers, state="readonly")
        self.cb_browser.set(self.browsers[0])
        self.cb_browser.grid(row=1, column=1, columnspan=2, pady=5, sticky="ew")

        self.lbl_url = tk.Label(self.form_frame, text=self.t["url"], width=18, anchor="w")
        self.lbl_url.grid(row=2, column=0, pady=5, sticky="w")
        self.ent_url = tk.Entry(self.form_frame)
        self.ent_url.grid(row=2, column=1, columnspan=2, pady=5, sticky="ew")

        self.btn_frame = tk.Frame(self)
        self.btn_frame.pack(pady=15)
        self.btn_vid = tk.Button(self.btn_frame, text=self.t["btn_vid"], width=20, bg="#4CAF50", fg="white", command=lambda: self.start_thread("video"))
        self.btn_vid.grid(row=0, column=0, padx=5)
        self.btn_aud = tk.Button(self.btn_frame, text=self.t["btn_aud"], width=20, bg="#2196F3", fg="white", command=lambda: self.start_thread("audio"))
        self.btn_aud.grid(row=0, column=1, padx=5)
        self.btn_upd = tk.Button(self.btn_frame, text=self.t["btn_upd"], width=20, bg="#FF9800", fg="white", command=lambda: self.start_thread("update"))
        self.btn_upd.grid(row=0, column=2, padx=5)

        self.lbl_log = tk.Label(self, text=self.t["log"])
        self.lbl_log.pack(anchor="w", padx=20)
        self.txt_log = scrolledtext.ScrolledText(self, height=12, bg="#1e1e1e", fg="#00ff00", font=("Consolas", 9))
        self.txt_log.pack(padx=20, pady=5, fill="both", expand=True)

    def change_lang(self, event):
        self.current_lang = self.cb_lang.get()
        self.t = LANGS[self.current_lang]
        self.update_texts()

    def change_theme(self, event):
        selected = self.cb_theme.get()
        self.is_dark_mode = True if selected == self.t["dark"] else False
        self.apply_theme()

    def update_texts(self):
        self.title(self.t["title"])
        self.lbl_dest.config(text=self.t["dest"])
        self.btn_browse.config(text=self.t["browse"])
        self.lbl_browser.config(text=self.t["browser"])
        self.lbl_url.config(text=self.t["url"])
        self.btn_vid.config(text=self.t["btn_vid"])
        self.btn_aud.config(text=self.t["btn_aud"])
        self.btn_upd.config(text=self.t["btn_upd"])
        self.lbl_log.config(text=self.t["log"])
        self.lbl_theme.config(text=self.t["theme"])
        self.btn_about.config(text=self.t["about"])
        
        theme_opts = [self.t["light"], self.t["dark"]]
        self.cb_theme.config(values=theme_opts)
        self.cb_theme.set(theme_opts[1] if self.is_dark_mode else theme_opts[0])

        current_browser_idx = self.cb_browser.current()
        self.browsers[0] = self.t["no_cookie"]
        self.cb_browser.config(values=self.browsers)
        self.cb_browser.current(current_browser_idx if current_browser_idx != -1 else 0)

    def show_about(self):
        messagebox.showinfo(self.t["about"], self.t["about_text"])

    def apply_theme(self):
        style = ttk.Style()
        if 'clam' in style.theme_names():
            style.theme_use('clam')

        if self.is_dark_mode:
            bg_color, fg_color = "#2b2b2b", "#ffffff"
            ent_bg, ent_fg = "#3c3f41", "#ffffff"
            sel_bg = "#555555"
        else:
            bg_color, fg_color = "#f0f0f0", "#000000"
            ent_bg, ent_fg = "#ffffff", "#000000"
            sel_bg = "#0078D7"

        self.configure(bg=bg_color)
        
        for frame in [self.top_frame, self.form_frame, self.btn_frame]:
            frame.configure(bg=bg_color)
            
        for lbl in [self.lbl_lang, self.lbl_theme, self.lbl_dest, self.lbl_browser, self.lbl_url, self.lbl_log]:
            lbl.configure(bg=bg_color, fg=fg_color)
            
        for ent in [self.ent_dest, self.ent_url]:
            ent.configure(bg=ent_bg, fg=ent_fg, insertbackground=ent_fg)

        self.btn_browse.configure(bg=ent_bg, fg=fg_color)
        self.btn_about.configure(bg=ent_bg, fg=fg_color)

        style.configure("TCombobox", fieldbackground=ent_bg, background=bg_color, foreground=ent_fg, arrowcolor=fg_color)
        style.map("TCombobox", fieldbackground=[("readonly", ent_bg)], selectbackground=[("readonly", sel_bg)], selectforeground=[("readonly", ent_fg)], foreground=[("readonly", ent_fg)])
                  
        self.option_add('*TCombobox*Listbox.background', ent_bg)
        self.option_add('*TCombobox*Listbox.foreground', ent_fg)
        self.option_add('*TCombobox*Listbox.selectBackground', sel_bg)
        self.option_add('*TCombobox*Listbox.selectForeground', fg_color)

    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.ent_dest.delete(0, tk.END)
            self.ent_dest.insert(0, folder)

    def log_message(self, msg):
        self.txt_log.insert(tk.END, msg + "\n")
        self.txt_log.see(tk.END)

    def start_thread(self, action):
        if not os.path.exists("yt-dlp.exe"):
            messagebox.showerror("Error", self.t["err_exe"])
            return

        dest = self.ent_dest.get().strip()
        url = self.ent_url.get().strip()
        browser = self.cb_browser.get()

        if action in ["video", "audio"]:
            if not dest:
                messagebox.showerror("Error", self.t["err_dest"])
                return
            if not url:
                messagebox.showerror("Error", self.t["err_link"])
                return

        threading.Thread(target=self.run_ytdlp, args=(action, dest, url, browser), daemon=True).start()

    def run_ytdlp(self, action, dest, url, browser):
        self.btn_vid.config(state=tk.DISABLED)
        self.btn_aud.config(state=tk.DISABLED)
        self.btn_upd.config(state=tk.DISABLED)
        self.txt_log.delete(1.0, tk.END)

        cmd = ["yt-dlp.exe"]
        
        if browser != self.t["no_cookie"]:
            cmd.extend(["--cookies-from-browser", browser])

        if action == "video":
            cmd.extend([
                "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
                "--merge-output-format", "mp4",
                "-o", f"{dest}/%(playlist_index)s - %(title)s.%(ext)s",
                url
            ])
        elif action == "audio":
            cmd.extend([
                "-x", "--audio-format", "mp3", "--audio-quality", "0",
                "--embed-thumbnail", "--add-metadata",
                "-o", f"{dest}/%(title)s.%(ext)s",
                url
            ])
        elif action == "update":
            cmd = ["yt-dlp.exe", "-U"]

        try:
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, creationflags=0x08000000)
            
            for line in process.stdout:
                self.txt_log.insert(tk.END, line)
                self.txt_log.see(tk.END)
                
            process.wait()
            self.log_message(f"\n{self.t['done']}")
        except Exception as e:
            self.log_message(f"\n[ERROR] {str(e)}")
            
        self.btn_vid.config(state=tk.NORMAL)
        self.btn_aud.config(state=tk.NORMAL)
        self.btn_upd.config(state=tk.NORMAL)

if __name__ == "__main__":
    app = YTDLApp()
    app.mainloop()