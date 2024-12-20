import themachinethatgoesping as pingmachine

folder = r"C:\Users\Schimel_Alexandre\Data\MBES\Kongsberg all\EM2040\KV-Meritaito_2024_EM2040_Sorvest-F-1-1-extracts-WCD"

files = pingmachine.echosounders.index_functions.find_files(folder, [".all", "wcd"])

fileHandler = pingmachine.echosounders.kongsbergall.KongsbergAllFileHandler(files,init=False)

d  = fileHandler.datagram_interface.datagrams("RuntimeParameters")[0]

print(d.get_model_number_as_string())
print(d.get_system_serial_number())
print(d.get_mode_as_ping_mode())
print(d.get_mode_as_tx_pulse_form())