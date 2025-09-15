#%%
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import time

def get_vector_input(vector_name):
    """
    Fungsi untuk meminta input 3 komponen (x, y, z) dari user
    dan mengembalikannya sebagai list of floats.
    Fungsi ini juga melakukan validasi input.
    """
    components = ['x', 'y', 'z']
    vector = []
    print(f"--- Masukkan komponen untuk {vector_name} ---")
    for comp in components:
        while True:
            try:
                value_str = input(f"Masukkan nilai {vector_name} {comp}: ")
                # Memungkinkan user keluar kapan saja dengan mengetik 'q'
                if value_str.lower() in ['q', 'quit', 'exit']:
                    return None
                value_float = float(value_str)
                vector.append(value_float)
                break  # Keluar dari loop while jika input valid
            except ValueError:
                print("Input tidak valid! Harap masukkan angka (contoh: 5, -10.2, atau 0).")
    return vector

print("Program Started")

client = RemoteAPIClient()
sim = client.getObject('sim')

# Menggunakan try-finally untuk memastikan simulasi selalu berhenti
try:
    # Menghentikan simulasi yang mungkin sudah berjalan
    sim.stopSimulation() 
    time.sleep(1) # Beri jeda sejenak

    sim.setStepping(False)
    sim.startSimulation()
    print("Simulasi dimulai.")

    # Tentukan handle objek di sini agar tidak perlu dicari berulang kali
    object_handle = sim.getObject("/Sphere[6]")

    # Periksa apakah objek ditemukan
    if object_handle == -1:
        print("Error: Objek '/Sphere[6]' tidak ditemukan di scene. Pastikan nama objek sudah benar.")
    else:
        print(f"Objek '{sim.getObjectAlias(object_handle)}' ditemukan dengan handle: {object_handle}")
        
        # Loop utama untuk terus meminta input dari user
        while True:
            print("\nSilakan masukkan nilai gaya dan torsi yang ingin diterapkan.")
            print("Ketik 'q' atau 'quit' pada input manapun untuk keluar dari program.")
            
            force_to_apply = get_vector_input("Gaya (Force)")
            if force_to_apply is None:
                break # Keluar dari loop utama jika user mengetik 'q'

            torque_to_apply = get_vector_input("Torsi (Torque)")
            if torque_to_apply is None:
                break # Keluar dari loop utama jika user mengetik 'q'
            
            # Terapkan gaya dan torsi ke objek
            sim.addForceAndTorque(object_handle, force_to_apply, torque_to_apply)
            
            # Tampilkan pesan konfirmasi
            message = f"Gaya {force_to_apply} dan Torsi {torque_to_apply} diterapkan."
            print(message)
            sim.addStatusbarMessage(message)
            
            time.sleep(0.1) # Jeda singkat sebelum loop berikutnya

finally:
    # Blok ini akan selalu dieksekusi, baik program selesai normal atau error
    sim.stopSimulation()
    print("\nSimulasi dihentikan. Program selesai.")