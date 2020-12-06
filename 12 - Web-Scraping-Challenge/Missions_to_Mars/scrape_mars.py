# Dependencies
import pandas as pd
from bs4 import BeautifulSoup as bs    # Beautiful Soup is a Python library for pulling data out of HTML and XML files
from splinter import Browser           # Splinter is python tool for testing web applications
from webdriver_manager.chrome import ChromeDriverManager
import time

def init_browser():
    # Boiler plate code that will be used whenever we use Splinter; allows 
    executable_path = {'executable_path': ChromeDriverManager().install()}   #Takes us to chromedriver manager that creates the browser window for our automated actions
    return Browser('chrome', **executable_path, headless=False)

scraped_data = {}  

def scrape():
    browser = init_browser()
      
    # Scrape: NASA Latest News
    nasa_url = 'https://mars.nasa.gov/news/'
    browser.visit(nasa_url)
    nasa_html = browser.html
    time.sleep(2)

    soup = bs(nasa_html, 'html.parser')

    latest_news_title = soup.find_all('div', class_='content_title')[1].text
    latest_ptext = soup.find('div', class_='article_teaser_body').text

    scraped_data['latest_news_title'] = latest_news_title
    scraped_data['latest_ptext'] = latest_ptext

    # Scrape: JPL Features Space Image
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_url)

    full_image_button = browser.find_by_id('full_image')
    full_image_button.click()

    more_info_button = browser.find_link_by_partial_text('more info')
    more_info_button.click()

    jpl_html = browser.html
    image_soup = bs(jpl_html, 'html.parser')

    latest_section = soup.select_one('ul.item_list li.slide')
    jpl_image_src = image_soup.select_one('figure.lede a img').get('src')
    featured_image_url = (f'https://jpl.nasa.gov{jpl_image_src}')

    scraped_data['featured_image_url'] = featured_image_url
    
    # Scrape: Mars Facts Table
    mars_facts_url = 'https://space-facts.com/mars/'
    browser.visit(mars_facts_url)

    table = pd.read_html(mars_facts_url)
    mars_facts_df = table[0]

    mars_facts_string = mars_facts_df.to_html()
    mars_facts_string = mars_facts_string.replace('\n', '')
    mars_facts_string

    scraped_data['mars_facts_string'] = mars_facts_string
    
    # Scrape: Mars Hemispheres
    mars_hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(mars_hemispheres_url)
    base_url = 'https://astrogeology.usgs.gov'
    hemisphere_image_urls = []

    # Hemisphere 1 of 4:  CEREBRUS
    click_1 = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[1]/a/img").click()
    time.sleep(3)

    click_2 = browser.find_by_id( "wide-image-toggle").click()
    time.sleep(3)

    cerberus_html = browser.html
    soup = bs(cerberus_html, "html.parser")

    cerberus_url = soup.find("img", class_="wide-image")["src"]
    cerberus_img_url = base_url + cerberus_url
    cerberus_title = soup.find("h2",class_="title").text
    cerberus = {"image_title":cerberus_title, "image_url": cerberus_img_url}

    hemisphere_image_urls.append(cerberus)

    browser.back()
    time.sleep(3)

    # Hemisphere 2 of 4: SCHIAPARELLI
    click_1 = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[2]/a/img").click()
    time.sleep(3)

    click_2 = browser.find_by_id( "wide-image-toggle").click()
    time.sleep(3)

    schiaparelli_html = browser.html
    soup = bs(schiaparelli_html, "html.parser")

    schiaparelli_url = soup.find("img", class_="wide-image")["src"]
    schiaparelli_img_url = base_url + schiaparelli_url
    schiaparelli_title = soup.find("h2",class_="title").text

    schiaparelli = {"image_title":schiaparelli_title, "image_url": schiaparelli_img_url}

    hemisphere_image_urls.append(schiaparelli)

    browser.back()
    time.sleep(3)

    # Hemisphere 3 of 4: SYRTIS
    click_1 = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[3]/a/img").click()
    time.sleep(3)

    click_2 = browser.find_by_id( "wide-image-toggle").click()
    time.sleep(3)

    syrtis_html = browser.html
    soup = bs(syrtis_html, "html.parser")

    syrtis_url = soup.find("img", class_="wide-image")["src"]
    syrtis_img_url = base_url + syrtis_url
    syrtis_title = soup.find("h2",class_="title").text
    syrtis = {"image_title":syrtis_title, "image_url": syrtis_img_url}

    hemisphere_image_urls.append(syrtis)

    browser.back()
    time.sleep(3)

    # Hemisphere 4 of 4: VALLES
    click_1 = browser.find_by_xpath( "//*[@id='product-section']/div[2]/div[4]/a/img").click()
    time.sleep(3)

    click_2 = browser.find_by_id( "wide-image-toggle").click()
    time.sleep(3)

    valles_html = browser.html
    soup = bs(valles_html, "html.parser")

    valles_url = soup.find("img", class_="wide-image")["src"]
    valles_img_url = base_url + valles_url
    valles_title = soup.find("h2",class_="title").text
    valles = {"image_title":valles_title, "image_url": valles_img_url}

    hemisphere_image_urls.append(valles)
    hemisphere_image_urls

    browser.quit()

    scraped_data['hemisphere_image_urls'] = hemisphere_image_urls

    return scraped_data

