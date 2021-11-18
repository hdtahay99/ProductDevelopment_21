library(shiny)
library(DT)

shinyUI(fluidPage(

    titlePanel("Tablas en DT"),
    
    tabsetPanel(
      tabPanel('Tablas DT',
               h2('Vista Basica'),
               DT::dataTableOutput('tabla1'),
               h2('Filtros'),
               DT::dataTableOutput('tabla2')
               ),
      tabPanel('click en tablas',
               fluidRow(
                  column(6, 
                         h2('Single Select Row'),
                         DT::dataTableOutput('tabla3'),
                         verbatimTextOutput('output1')
                         ),
                  column(6, 
                         h2('Multiple Select Row'),
                         DT::dataTableOutput('tabla4'),
                         verbatimTextOutput('output2')
                         )
                ),
             
                fluidRow(
                  column(6, 
                         h2('Single Select Column'),
                         DT::dataTableOutput('tabla5'),
                         verbatimTextOutput('output3')
                  ),
                  column(6, 
                         h2('Multiple Select Column'),
                         DT::dataTableOutput('tabla6'),
                         verbatimTextOutput('output4')
                  )
                ),
               fluidRow(
                 column(6, 
                        h2('Single Select cell'),
                        DT::dataTableOutput('tabla7'),
                        verbatimTextOutput('output5')
                 ),
                 column(6, 
                        h2('Multiple Select cell'),
                        DT::dataTableOutput('tabla8'),
                        verbatimTextOutput('output6')
                 )
               ),
               fluidRow(
                 column(6, 
                        h2('Single Select row+column'),
                        DT::dataTableOutput('tabla9'),
                        verbatimTextOutput('output7')
                 ),
                 column(6, 
                        h2('Multiple Select row+column'),
                        DT::dataTableOutput('tabla10'),
                        verbatimTextOutput('output8')
                 )
               )
               )
    )

))
