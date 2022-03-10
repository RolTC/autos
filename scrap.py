import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www2.jus.gov.ar/dnrpa-site/#!/estimador")
elem = driver.find_element_by_name("codigoTramite")
elem.send_keys("TRAS")
elem = driver.find_element_by_name("dominio")
elem.send_keys("C063573")
elem = driver.find_element_by_name("valorDeclarado")
elem.send_keys("1000")
elem = driver.find_element_by_name("codigoProvincia")
elem.send_keys("BUENOS")
elem = driver.find_element_by_class_name("btn-success")
elem.send_keys(Keys.RETURN)
if not "No se puede" in driver.page_source:
  delay = 3 # seconds
  try:
    myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))
    print "Page is ready!"
    table = driver.find_element_by_css_selector(".table-striped")
    with open('data/eggs.csv', 'w', newline='') as csvfile:
        wr = csv.writer(csvfile)
        for row in table.find_elements_by_css_selector('tr'):
            wr.writerow([d.text for d in row.find_elements_by_css_selector('td')])
  except TimeoutException:
    print "Loading took too much time!"


delay = 10 # seconds
file_time = []
no_reg = []

for x in range(301, 400):
  p = "C0635"+str(x)
  driver.get("https://www2.jus.gov.ar/dnrpa-site/#!/estimador")
  elem = driver.find_element_by_name("codigoTramite")
  elem.send_keys("TRAS")
  elem = driver.find_element_by_name("dominio")
  elem.send_keys(p)
  elem = driver.find_element_by_name("valorDeclarado")
  elem.send_keys("1000")
  elem = driver.find_element_by_name("codigoProvincia")
  elem.send_keys("BUENOS")
  elem = driver.find_element_by_class_name("btn-success")
  elem.send_keys(Keys.RETURN)
  if not "No se puede" in driver.page_source:
    try:
      table = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.media')))
      table = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.table-striped')))
      with open('data/'+p+'.csv', 'w', newline='') as csvfile:
          wr = csv.writer(csvfile)
          wr.writerow([for d in table.find_elements_by_css_selector('.text-right')])
          wr.writerow([for d in table.find_elements_by_css_selector('.ng-binding')])
    except TimeoutException:
      print('next')
      if not "No se puede" in driver.page_source:
        no_reg.append(x)
      else:
        file_time.append(x)

    
  
  

  for d in table.find_elements_by_css_selector('.text-right'):
    print([d.text for d in table.find_elements_by_css_selector('.text-right')])





#Intento de mejorar el tiempo (LISTO)

delay = 15 # seconds
file_time = []
#no_reg = []

for x in range(521, 700):
  p = "C0635"+str(x)
  driver.get("https://www2.jus.gov.ar/dnrpa-site/#!/estimador")
  elem = driver.find_element_by_name("codigoTramite")
  elem.send_keys("TRAS")
  elem = driver.find_element_by_name("dominio")
  elem.send_keys(p)
  elem = driver.find_element_by_name("valorDeclarado")
  elem.send_keys("1000")
  elem = driver.find_element_by_name("codigoProvincia")
  elem.send_keys("BUENOS")
  elem = driver.find_element_by_class_name("btn-success")
  elem.send_keys(Keys.RETURN)
  try:
    table = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.media')))
    if "No se puede" in driver.page_source:
      no_reg.append(x)
    else:
      table = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.table-striped')))
      with open('data/'+p+'.csv', 'w', newline='') as csvfile:
        wr = csv.writer(csvfile)
        wr.writerow([d.text for d in table.find_elements_by_css_selector('.text-right')])
        wr.writerow([d.text for d in table.find_elements_by_css_selector('.ng-binding')])
  except TimeoutException:
    print('next')
    file_time.append(x)

    
  


no_reg
file_time




  




  
