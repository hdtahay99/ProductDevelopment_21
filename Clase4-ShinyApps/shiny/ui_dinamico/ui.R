library(shiny)

shinyUI(fluidPage(

    titlePanel("UI Dinamico"),
    
    tabsetPanel(
      tabPanel("Ejemplo 1", 
               numericInput("min1", "limite inferior", value=5),
               numericInput("max1", "limite superior", value=10),
               sliderInput("slider1", "Seleccione intervalo",
                           min=0, max=15, value=5)
               ),
      tabPanel("Ejemplo 2", 
               sliderInput("s1", "Seleccione intervalo",
                           min=-5, max=15, value=5),
               sliderInput("s2", "Seleccione intervalo",
                           min=-5, max=15, value=5),
               sliderInput("s3", "Seleccione intervalo",
                           min=-5, max=15, value=5),
               sliderInput("s4", "Seleccione intervalo",
                           min=-5, max=15, value=5),
               actionButton("reset", "Reiniciar")
               
               ),
      tabPanel("Ejemplo 3", 
               numericInput("n", "Corridas", value=10),
               actionButton("correr", "correr")
               ),
      tabPanel("Ejemplo 4", 
               numericInput("nvalue", "value", value=0)),
      tabPanel("Ejemplo 5", 
               numericInput("celcius", "Temperatura en celsius", value=NA),
               numericInput("farenheit", "Temperatura en farenheit", value=NA)
               ),
    )

))
