library(tidyverse)

inp = read_lines("C:/Users/aiden/Dropbox/git/adventofcode/day11_input.txt") 
dep <- as.integer(inp[1])
bus <- inp[2] %>% str_split(",") %>% unlist()
bus <- bus[grepl("\\d+", bus)]
dep_diff <- 1e6
for(b in bus){
  b <- as.integer(b)
  dep_tmp <- b * ceiling(dep / b)
  diff_tmp <- dep_tmp - dep
  if(diff_tmp < dep_diff) {
    dep_bus <- b
    dep_diff <- diff_tmp
  }
}
print(glue("Bus {dep_bus} depart at time diff {dep_diff}"))

## Part 2 - use online calculator
bus <- inp[2] %>% str_split(",") %>% unlist()
catch <- imap(bus, function(.x, .y){
  i <- as.integer(.y)
  x <- .x
  if (str_detect(x, "\\d+"))
    print(glue("bus {.x} offset {i - 1}"))
})

# https://www.dcode.fr/chinese-remainder