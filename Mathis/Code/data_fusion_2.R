# Clean environment #
rm(list=ls())

# Import #

co_emissions <- read_csv("Desktop/Dashboard/Archive2/Situation_annual-co-emissions-by-region.csv")
death_rates <- read_csv("Desktop/Dashboard/Archive2/death-rates-total-air-pollution.csv")
ozone <- read_csv("Desktop/Dashboard/Archive2/ozone-o3-concentration-in-ppb.csv")

# Selection #

colnames(co_emissions) = c("Entity", "Code", "Year", "CO2")
colnames(death_rates) = c("Entity", "Code", "Year", "Death")
colnames(ozone) = c("Entity", "Code", "Year", "Ozone")

# Filter year #

co_emissions = co_emissions %>% dplyr::filter(Year == 2016)
death_rates = death_rates %>% dplyr::filter(Year == 2016)
ozone = ozone %>% dplyr::filter(Year == 2015)


# Harmonization #

dataset = left_join(co_emissions, death_rates, by = "Entity", copy = T)
dataset = left_join(dataset, ozone, by = "Entity", copy = T)

dataset = dataset %>% dplyr::select(Entity, Code.x, Year.x, CO2, Death, Ozone)
dataset = na.omit(dataset)
colnames(dataset) = c("Country_Region", "Code", "Year", "CO2", "Death", "Ozone")
rm(co_emissions, death_rates, ozone)


# Compare #

File <- read_csv("Desktop/Dashboard/Archive2/File.csv")
colnames(File)[12] = "GDP_BILLIONS"

dataset = left_join(File, dataset, by = "Country_Region", copy = T)
dataset = dataset %>% dplyr::select(Country_Region, FIPS, Lat, Long_, COUNTRY, GDP_BILLIONS, CO2, Death, Ozone, CODE)

dataset$GDP_BILLIONS[is.na(dataset$GDP_BILLIONS)] <- mean(dataset$GDP_BILLIONS,na.rm = T)
dataset$CO2[is.na(dataset$CO2)] <- mean(dataset$CO2,na.rm = T)
dataset$Death[is.na(dataset$Death)] <- mean(dataset$Death,na.rm = T)
dataset$Ozone[is.na(dataset$Ozone)] <- mean(dataset$Ozone,na.rm = T)

colnames(dataset) = c("Country_Region", "FIPS", "Lat", "Long_", "COUNTRY", "GDP_BILLIONS", "CO2_emissions", "Death_from_air_pollution", "Ozone_concentration", "CODE")
# Export #
write.csv(x = dataset, file = "data_situation2.csv")

