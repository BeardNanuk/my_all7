module my_lib 
  implicit none
  public :: linspace

  contains 

  ! create a 1-D array with evenly spaced elements

  subroutine linspace(x, x_start, x_end, x_len)
    real, dimension(:), intent(out) :: x
    real :: x_start, x_end, dx
    integer :: x_len, i
   
    dx = (x_end - x_start) / (x_len - 1)
    x(1:x_len) = [(x_start + ((i-1)*dx), i=1,x_len)]
  end subroutine


end module my_lib 

