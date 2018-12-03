! module is like a toolbox, create tools, then load them. 
module gnuplot_fortran 
  implicit none
  contains
  subroutine plot2d(x,y)

    real, intent(in),dimension(:) :: x,y  
    integer :: size_x, size_y, i
    size_x = size(x)
    size_y = size(y)
    if (size_x /= size_y) then
      print *, "Array size mismatch"
    else
      open(unit=1, file='data.dat')
      do i = 1,size(x)
        ! space deliminator here
        write(1,*) x(i),' ',y(i)
      end do 
      close(unit=1)
    end if 

  end subroutine plot2d

end module gnuplot_fortran 



