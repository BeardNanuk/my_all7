! plot sine function 

program array 
  implicit none
  ! with 'parameter', this is a constant whose value would not change in this
  ! program
  real, parameter :: pi = 4*atan(1.0)
  !array clarification with 'dimension'
  integer, parameter :: n = 100
  real, dimension(1:n) :: x, y
  real :: a = 0.0, b = 2*pi
  real :: increment 
  integer :: i 

  increment = (b - a)/(real(n) - 1)
  
  !first element is set to zero
  x(1) = 0.0 
  ! populate x 
  do i = 2,n
    x(i) = x(i-1) + increment
  end do 
  
  y = sin(x)

 !print *, x(1:5)
 !print *, y(1:5)

  open(unit=1, file='data.dat')
  do i = 1,n
    write(1,*) x(i),y(i)
  end do
  close(unit=1)
   







end program array



