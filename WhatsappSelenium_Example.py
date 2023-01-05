"""########################################

Whatsapp Selenium Test by @theXXLMAN

###########################################
"""

from selenium import webdriver

# Abrimos la ventana del navegador
driver = webdriver.Firefox()

# Vamos a la página web de WhatsApp
driver.get("https://web.whatsapp.com/")

# Esperamos a que el usuario escanee el código QR para iniciar sesión
input("Por favor, escanea el código QR y luego presiona Enter para continuar...")

# Buscamos el contacto o grupo al que queremos enviar el mensaje
elem = driver.find_element_by_xpath('//span[contains(text(), "Nombre del contacto o grupo")]')
elem.click()

# Encontramos el campo de texto donde vamos a escribir el mensaje
text_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

# Escribimos el mensaje
text_box.send_keys("Hola, ¿cómo estás?")

# Enviamos el mensaje
driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()

# Cerramos el navegador
driver.quit()
