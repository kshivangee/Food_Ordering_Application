library(knitr)
library(kableExtra)
library(dplyr)
library(ggplot2)
library(plotrix)

df = read.csv("h1b.csv", header = TRUE, sep = ",")

#group the data on CASE_STATUS to see the distribution of CASE_STATUS.
df %>% filter(!is.na(CASE_STATUS)) %>% group_by(CASE_STATUS) %>% 
summarise(nr = length(lat)) %>% ungroup() -> dc
ggplot(data = dc, aes(x = reorder(CASE_STATUS,nr), y = nr/1000)) +  
geom_bar(stat="identity", fill="tomato", colour="black") +
coord_flip() + theme_bw(base_size = 10)  +
labs(title="", x ="Case status", y = "Number of applications (thousands)")


#top 20 of most frequent job titles in visa applications
df %>% group_by(JOB_TITLE) %>% summarise(nr = length(lat)) %>% 
top_n(n=20) %>% arrange(-nr) %>% ungroup() -> dj
ggplot(data = dj, aes(x = reorder(JOB_TITLE,nr), y = nr)) +  
geom_bar(stat="identity", fill="gold", colour="black") +
coord_flip() + theme_bw(base_size = 10)  +
labs(title="", x ="Job title (top 20)", y = "Number of applications")



#percent of full-time positions from the total number of applications
df %>% filter(!is.na(FULL_TIME_POSITION)) %>% group_by(FULL_TIME_POSITION) %>% summarise(nr = length(lat)) %>% ungroup() -> dp
lbls = c("Part time","Full time")
pcts = round(dp$nr / sum(dp$nr) * 100,0)
lbls = paste(lbls, pcts)
lbls = paste(lbls,"%", sep="")
cols = c("tomato", "gold")
pie3D(x=dp$nr, labels=lbls, col = cols, explode=0, main = "Positions type")
