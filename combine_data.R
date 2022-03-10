
library(dplyr)
library(janitor)

f<-list.files("data")

aux<- lapply(f, function(x){
  d<-read.csv(paste0("data/",x), stringsAsFactors = F)
  d<-clean_names((d))
  d$patente <- gsub('.csv','',x)
  if('modelo'%in% names(d))
    d$modelo<-as.character(d$modelo)
  return(d)
})


df<-bind_rows(aux)

df<-df[,-c(1,2,3)]



