program plotter

use gnuplot_fortran

implicit none

integer,parameter :: n = 100
real, dimension(0:n) :: x, y
! do not forget to put 0.0 when defining float 
real :: x_start = 0.0, x_end = 20, dx
integer :: i 

! make x array
dx = (x_end - x_start)/n
x(0:n) = [(i*dx, i=0,n)]
 
! make y array 
y = sin(x) / (x + 1)

! generate data for plot 
call plot2d(x,y)





end program plotter
