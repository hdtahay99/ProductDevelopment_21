library(shiny)
library(DT)

shinyUI(fluidPage(

    titlePanel("Interacciones Shiny Plots - Tarea"),
    
    tabPanel('Interacciones y cambios de color',
             plotOutput('plot_interaction',
                        click='clk',
                        dblclick = 'dclk',
                        hover='mouse_hover',
                        brush='mouse_brush'),
             hr(),
             h4('Table Mtcars'),
             DT::dataTableOutput('mtcars_tbl'),
             )

))
