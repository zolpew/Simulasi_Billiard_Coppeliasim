# Simulasi_Billiard_Coppeliasim
Game Billiard Menggunakan Coppeliasim dan python user interface

# CoppeliaSim Interactive Force & Torque Controller

Sebuah skrip Python sederhana untuk mengontrol objek di dalam simulasi CoppeliaSim secara interaktif melalui terminal. Anda dapat menerapkan nilai gaya (force) dan torsi (torque) secara real-time tanpa perlu me-restart skrip atau simulasi.

*Read this in other languages: [English](#english-version)*

---

## 📜 Deskripsi

Proyek ini menggunakan ZMQ Remote API dari CoppeliaSim untuk menjembatani skrip Python dengan *scene* simulasi yang sedang berjalan. Skrip ini menyediakan antarmuka baris perintah (CLI) yang meminta pengguna untuk memasukkan komponen X, Y, dan Z untuk gaya dan torsi. Nilai-nilai ini kemudian langsung diterapkan pada objek yang telah ditentukan di dalam simulasi.

Ini sangat berguna untuk melakukan *prototyping*, pengujian, atau sekadar bereksperimen dengan fisika simulasi secara dinamis.

![Contoh Penggunaan Skrip di Terminal dan Hasilnya di CoppeliaSim]

## ✨ Fitur Utama

-   **Kontrol Interaktif**: Masukkan nilai gaya dan torsi langsung dari terminal Anda.
-   **Aplikasi Real-Time**: Gaya dan torsi diterapkan secara instan ke objek di CoppeliaSim.
-   **Loop Berkelanjutan**: Terapkan gaya dan torsi berulang kali tanpa harus memulai ulang skrip.
-   **Validasi Input**: Skrip dapat menangani input yang salah (non-numerik) tanpa *crash*.
-   **Keluar dengan Aman**: Opsi untuk menghentikan skrip dengan rapi menggunakan perintah `q` atau `quit`.
-   **Manajemen Sesi**: Skrip secara otomatis memulai dan menghentikan simulasi, memastikan sesi selalu ditutup dengan benar.

## 🛠️ Persyaratan

Sebelum memulai, pastikan Anda telah menginstal:

1.  **CoppeliaSim**: Versi Edu atau Pro (dites pada CoppeliaSim 4.x).
2.  **Python**: Versi 3.6 atau yang lebih baru.
3.  **Library ZMQ Client**: Library Python untuk berkomunikasi dengan CoppeliaSim.

## 🚀 Instalasi & Pengaturan

1.  **Clone Repositori Ini (Opsional)**
    ```bash
    git clone [URL_REPOSITORI_ANDA]
    cd [NAMA_FOLDER_REPOSITORI]
    ```

2.  **Instal Library yang Dibutuhkan**
    Buka terminal atau Command Prompt Anda dan jalankan perintah berikut untuk menginstal library `coppeliasim-zmqremoteapi-client`:
    ```bash
    pip install coppeliasim-zmqremoteapi-client
    ```

## 🎮 Cara Menggunakan

1.  **Buka CoppeliaSim**: Jalankan aplikasi CoppeliaSim dan buka *scene* yang berisi objek yang ingin Anda kontrol.
2.  **Identifikasi Objek**: Pastikan Anda tahu nama path objek target. Secara default, skrip ini menargetkan objek bernama `/Sphere[6]`.
3.  **Jalankan Skrip Python**: Buka terminal atau Command Prompt, arahkan ke direktori tempat Anda menyimpan file `.py`, lalu jalankan:
    ```bash
    Tugas_SRO_Simulalsi_Pool_Table.py
    ```
4.  **Masukkan Nilai**: Terminal akan meminta Anda untuk memasukkan nilai untuk setiap komponen gaya (Fx, Fy, Fz) dan torsi (Tx, Ty, Tz).
    ```
    --- Masukkan komponen untuk Gaya (Force) ---
    Masukkan nilai Gaya (Force) x: 10
    Masukkan nilai Gaya (Force) y: 0
    Masukkan nilai Gaya (Force) z: 50
    --- Masukkan komponen untuk Torsi (Torque) ---
    Masukkan nilai Torsi (Torque) x: 0
    Masukkan nilai Torsi (Torque) y: 5
    Masukkan nilai Torsi (Torque) z: 0
    ```
5.  **Amati Simulasi**: Lihat objek bergerak di CoppeliaSim sesuai dengan input yang Anda berikan.
6.  **Ulangi atau Keluar**: Skrip akan langsung meminta input baru. Untuk berhenti, cukup ketik `q` atau `quit` pada prompt mana pun dan tekan Enter.

## 🔧 Kustomisasi

Anda dapat dengan mudah mengubah objek target. Cukup edit baris berikut di dalam skrip dengan *path* objek yang Anda inginkan:

```python
# Ganti "/Sphere[6]" dengan path objek target Anda
object_handle = sim.getObject("/Sphere[6]")
```

---
---

## English Version

# CoppeliaSim Interactive Force & Torque Controller

A simple Python script to interactively control an object within a CoppeliaSim simulation via the terminal. You can apply force and torque values in real-time without restarting the script or the simulation.

## 📜 Description

This project utilizes CoppeliaSim's ZMQ Remote API to bridge a Python script with a running simulation scene. The script provides a command-line interface (CLI) that prompts the user to input X, Y, and Z components for both force and torque. These values are then immediately applied to a specified object in the simulation.

This is highly useful for prototyping, testing, or simply experimenting with simulation physics dynamically.

## ✨ Key Features

-   **Interactive Control**: Input force and torque values directly from your terminal.
-   **Real-Time Application**: Forces and torques are instantly applied to the object in CoppeliaSim.
-   **Continuous Loop**: Apply different forces and torques repeatedly without restarting the script.
-   **Input Validation**: The script handles invalid (non-numeric) user input without crashing.
-   **Graceful Exit**: Option to stop the script cleanly using `q` or `quit` commands.
-   **Session Management**: The script automatically starts and stops the simulation, ensuring the session is always closed properly.

## 🛠️ Requirements

Before you begin, ensure you have installed:

1.  **CoppeliaSim**: Edu or Pro version (tested on CoppeliaSim 4.x).
2.  **Python**: Version 3.6 or newer.
3.  **ZMQ Client Library**: The Python library for communicating with CoppeliaSim.

## 🚀 Installation & Setup

1.  **Clone This Repository (Optional)**
    ```bash
    git clone [YOUR_REPOSITORY_URL]
    cd [REPOSITORY_FOLDER_NAME]
    ```

2.  **Install Required Library**
    Open your terminal or Command Prompt and run the following command to install the `coppeliasim-zmqremoteapi-client` library:
    ```bash
    pip install coppeliasim-zmqremoteapi-client
    ```

## 🎮 How to Use

1.  **Open CoppeliaSim**: Run the CoppeliaSim application and open the scene containing the object you wish to control.
2.  **Identify the Object**: Make sure you know the path name of the target object. By default, the script targets an object named `/Sphere[6]`.
3.  **Run the Python Script**: Open a terminal, navigate to the directory where you saved the `.py` file, and run:
    ```bash
    python your_script_name.py
    ```
4.  **Enter Values**: The terminal will prompt you to enter values for each component of force (Fx, Fy, Fz) and torque (Tx, Ty, Tz).
5.  **Observe the Simulation**: Watch the object move in CoppeliaSim according to the inputs you provided.
6.  **Repeat or Exit**: The script will immediately ask for new inputs. To stop, simply type `q` or `quit` at any prompt and press Enter.

## 🔧 Customization

You can easily change the target object. Simply edit the following line in the script with your desired object's path:

```python
# Change "/Sphere[6]" to your target object's path
object_handle = sim.getObject("/Sphere[6]")
```
