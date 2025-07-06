import os
from colorama import init, Fore, Style
import pyperclip

# Telethon
from telethon.sync import TelegramClient
from telethon.sessions import StringSession as TelethonStringSession

# Pyrogram (v2.x)
from pyrogram import Client as PyroClient

init(autoreset=True)

def banner():
    print(Fore.CYAN + """
███████╗ ██████╗ ███╗   ██╗██████╗  ██████╗ ████████╗
██╔════╝██╔═══██╗████╗  ██║██╔══██╗██╔═══██╗╚══██╔══╝
█████╗  ██║   ██║██╔██╗ ██║██║  ██║██║   ██║   ██║   
██╔══╝  ██║   ██║██║╚██╗██║██║  ██║██║   ██║   ██║   
██║     ╚██████╔╝██║ ╚████║██████╔╝╚██████╔╝   ██║   
╚═╝      ╚═════╝ ╚═╝  ╚═══╝╚═════╝  ╚═════╝    ╚═╝   
    """)
    print(Fore.MAGENTA + "✨ TELETHON & PYROGRAM STRING SESSION GENERATOR by @Zidan Alfariza Putra Pratama\n" + Style.RESET_ALL)

def generate_telethon(api_id, api_hash):
    session_name = "telethon_custom"
    with TelegramClient(TelethonStringSession(), api_id, api_hash) as client:
        print(Fore.CYAN + "\n🔐 Silakan login ke akun Telegram kamu (Telethon)...")
        client.start()
        string = client.session.save()
        return string, session_name

def generate_pyrogram(api_id, api_hash):
    session_name = "pyrogram_custom"
    print(Fore.CYAN + "\n🔐 Silakan login ke akun Telegram kamu (Pyrogram)...")
    with PyroClient(session_name, api_id=api_id, api_hash=api_hash) as app:
        string = app.export_session_string()
        return string, session_name

def main():
    banner()
    try:
        print(Fore.YELLOW + "📌 Pilih jenis session:")
        print("1. Telethon")
        print("2. Pyrogram")
        choice = input(Fore.GREEN + "Masukkan pilihan (1/2): ")

        api_id = int(input(Fore.YELLOW + "\n🔢 Masukkan API_ID: "))
        api_hash = input(Fore.YELLOW + "🔑 Masukkan API_HASH: ")

        if choice == "1":
            string, session_name = generate_telethon(api_id, api_hash)
            lib = "telethon"
        elif choice == "2":
            string, session_name = generate_pyrogram(api_id, api_hash)
            lib = "pyrogram"
        else:
            print(Fore.RED + "❌ Pilihan tidak valid!")
            return

        print(Fore.GREEN + f"\n✅ String session ({lib}) berhasil dibuat:\n")
        print(Fore.WHITE + Style.BRIGHT + string)

        filename = f"{session_name}_string.txt"
        with open(filename, "w") as f:
            f.write(string)
            print(Fore.BLUE + f"\n💾 String session disimpan ke '{filename}'")

        try:
            pyperclip.copy(string)
            print(Fore.MAGENTA + "📋 String session sudah disalin ke clipboard!")
        except Exception:
            print(Fore.RED + "⚠️ Tidak bisa menyalin ke clipboard (pyperclip error)")

    except Exception as e:
        if "FLOOD_WAIT" in str(e):
            try:
                wait_time = int(str(e).split("FLOOD_WAIT_")[1].split()[0])
                print(Fore.RED + f"\n⏳ Telegram membatasi login. Tunggu sekitar {wait_time} detik (~{wait_time // 60} menit).")
            except:
                print(Fore.RED + f"\n⏳ Telegram membatasi login: {e}")
        else:
            print(Fore.RED + f"\n❌ Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()
