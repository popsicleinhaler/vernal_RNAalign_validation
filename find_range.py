from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import re
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s=Service(ChromeDriverManager().install())
options = Options()
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options,service=s)
webpage = 'http://vernal.cs.mcgill.ca/gallery/default_name_pruned'
driver.get(webpage)

wait_length = 0

def wait_click(ep):
    wait = WebDriverWait(driver, 30, poll_frequency=0.1)#, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
    element = wait.until(EC.element_to_be_clickable((By.XPATH, ep)))
    element.click()
    pass

def wait_e(ep):
    wait = WebDriverWait(driver, 30, poll_frequency=0.1)#, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
    element = wait.until(EC.presence_of_element_located((By.XPATH, ep)))
    return element

def get_instance_num(motif_n=5, cluster_n=1):
    
    motif = '/html/body/p[2]/button['+str(motif_n)+']'
    wait_click(motif)

    cluster = '/html/body/p[2]/table[5]/tbody/tr['+str(cluster_n)+']/td/a'
    wait_click(cluster)

    instance_num = wait_e('/html/body/div/div[1]').text

    for i in range(1):
        driver.back()

    return int(re.findall(r'\d+',instance_num)[0])


def get_id_res(motif_n=6, cluster_n=1, instance_n=1):

    motif = '/html/body/p[2]/button['+str(motif_n)+']'
    wait_click(motif)

    cluster = '/html/body/p[2]/table[5]/tbody/tr['+str(cluster_n)+']/td/a'
    wait_click(cluster)

    instance = '/html/body/div/div[1]/a['+str(instance_n)+']'
    wait_click(instance)

    residues_list = wait_e('/html/body/div/table/tbody/tr[2]/td[3]').text
    PDBID = wait_e('/html/body/div/table/tbody/tr[2]/td[2]/a').text

    for i in range(2):
        driver.back()

    return [PDBID, residues_list]

# actually probably not in motif-5 because has 5 residues so must be something lower ->  get it?
#main issue is that there doesn't seem to be that much
# work around is to find the matching name from website to the local dictionary
ll=[]
for c in range(1,129):
    print('this is where it stopped in the clusters:', c)
    for i in range(2,get_instance_num(cluster_n=c)+1):
        print('instance where it stopped:',i)
        l = get_id_res(motif_n=5,cluster_n=c, instance_n=i)[0]
        ll.append(l)
        print(ll)
        if l == '5ib8':
            print(l)
