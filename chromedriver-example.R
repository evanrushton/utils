library(rvest)
library(RSelenium)
library(xml2)
library(magrittr)

# You may need to download a different chromedriver version from https://chromedriver.chromium.org/downloads
# For my old mac with an old chrome version I made a directory in:
#   /Users/ERushton/Library/Application Support/binman_chromedriver/mac64/99.0.4844.51

# Create and launch remote driver
rD <- rsDriver(browser='chrome', port=4567L, chromever="99.0.4844.51")
remDr <- rD[['client']]
salsa_url <- "https://salsacycles.com/bikes/all"
remDr$navigate(salsa_url)
Sys.sleep(4)             # load time
remDr$maxWindowSize()    # visualize elements
html <- read_html(remDr$getPageSource()[[1]])

part_name <- html %>% html_nodes(".title-0-2-159") %>% html_text()
part_price <- html %>% html_nodes(".subtitle-0-2-160") %>% html_text()

# Close driver and stop server
remDr$close()
rD$server$stop()
rm(rD)
rm(remDr)

# Export table
df <- data.frame(Name = part_name, Price = part_price)
write.csv(df, "bikes.csv")
