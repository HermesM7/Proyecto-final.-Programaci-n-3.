from selenium import webdriver
import os

driver = webdriver.Chrome()

url = "http://127.0.0.1:5500/Final%20Project%20P3/VeggieLife/carrito.html"

try:
    
    driver.get(url)
    
    boton_empty_cart = driver.find_element_by_xpath("//button[contains(text(),'empty cart')]")
    boton_empty_cart.click()
    print("Se hizo clic en el botón 'empty cart'")
    
    directorio_capturas = "capturas_de_pantalla"
    
    if not os.path.exists(directorio_capturas):
        os.makedirs(directorio_capturas)
    
    nombre_archivo = "Add_empty_cart.png"
 
    ruta_captura = os.path.join(directorio_capturas, nombre_archivo)

    driver.save_screenshot(ruta_captura)
    print("Captura de pantalla tomada y guardada en:", ruta_captura)
    
except Exception as e:
    print("Ocurrió un error:", e)
    
finally:

    driver.quit()
