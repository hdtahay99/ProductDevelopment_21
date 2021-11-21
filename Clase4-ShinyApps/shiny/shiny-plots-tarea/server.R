library(shiny)
library(ggplot2)

## Variable global para persistencia de puntos clickeados
idx_points <- NULL
idx_dclk <- NULL
idx_brush <- NULL
idx_clk<- NULL

shinyServer(function(input, output) {
  
  hover_point<-reactiveValues(idx = NULL)
  
  
  selected_points <- reactive({
    
    idx_clk <<- nearPoints(mtcars, input$clk,xvar = 'wt', yvar = 'mpg')
    idx_dclk <<- nearPoints(mtcars, input$dclk,xvar = 'wt', yvar = 'mpg')
    idx_brush<<-brushedPoints(mtcars, input$mouse_brush, xvar = 'wt', yvar = 'mpg')
    
    if(dim(idx_clk)[1])
    {
      if(dim(idx_points[(row.names(idx_points) %in% row.names(idx_clk)), ])[1] == 0){
        idx_points <<- rbind(idx_points, idx_clk)
      }
    }
    else{
      idx_points <<- rbind(idx_points, idx_clk)
    }
    
    if(dim(idx_brush)[1])
    {
      if(dim(idx_points[(row.names(idx_points) %in% row.names(idx_brush)), ])[1] == 0){
        idx_points <<- rbind(idx_points, idx_brush)
      }
    }
    
    if(dim(idx_dclk)[1]){
      idx_points <<- idx_points[!(row.names(idx_points) %in% row.names(idx_dclk)), ]
    }
    
    return(idx_points)
  })
  
  observe({
    idx<-c(input$mouse_hover$x, input$mouse_hover$y)
    if(!is.null(idx)){
      hover_point$idx<-nearPoints(mtcars, input$mouse_hover, xvar = 'wt', yvar = 'mpg')
    }
  })
  
  output$plot_interaction <- renderPlot({
    plot<-ggplot(mtcars, aes(x = wt, y = mpg)) +
      geom_point(colour="#E7B800", size=5) +
      geom_point(data = selected_points(), colour = "green", size = 5)+
      theme_minimal()
    
    if(!is.null(hover_point$idx)){
      plot<- plot + geom_point(data = hover_point$idx, colour = "gray", size = 5)
    }
    
    plot
  })
  
  output$mtcars_tbl<-DT::renderDataTable({
    selected_points()
  })
  
  

})
