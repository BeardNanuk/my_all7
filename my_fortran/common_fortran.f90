! plot sine function 

program common_fortran

!############# common fortran ###########################



! print to the screen
print *, v
!output
gfortran foofilename.f90 -o barcompliedfile


!##### data types




! floating point number
real :: rho_s = 2.7 ! units 
! square 
v = D**2/(19*n)
! do not forget to put 0.0 when defining float 
real :: x_start = 0.0, x_end = 20, dx

! # constant creation 
! with 'parameter', this is a constant whose value would not change in this
! program
real, parameter :: pi = 4*atan(1.0)


! ## array creation method 1 
!array clarification with 'dimension'
integer, parameter :: n = 100
real, dimension(1:n) :: x, y
! ## array creation method 2 
! do not forget to put 0.0 when defining float 
real :: x_start = 0.0, x_end = 20, dx







!##### if, for, while ...


!## if else
  if (disc < 0) then
    print *, 'roots are imaginary'
  else
    root1 = (-b + sqrt(disc))/2*a
    root2 = (-b - sqrt(disc))/2*a
    ! do not forget to use commas to seperate different items for
    ! printing
    print *, 'roots are ', root1, 'and ', root2
  end if

!## looping 

  do fret=1,total_frets
  # print things after? 
  print *, fret, scale_length/(fconst**fret)
  end do



!### program structure

program fretcalc !program name 
  implicit none
  real :: scale_length = 25.5 ! [inches]
  real :: fconst = 2.0**(1.0/12.0)
  integer :: total_frets = 24
  
  do fret=1,total_frets
    # print things after? 
    print *, fret, scale_length/(fconst**fret)
  end do

 

end program fretcalc

!# compiling a regular fortran file, then output an excutable file. 
gfortran foofilename.f90 -o barcompliedfile
!# compile a module 
ifort -c gnuplot_fortran.f90
! here is the output
gnuplot_fortran.mod gnuplot_fortran.o
! compile two files into one file
gfortran -o plotter gnuplot_fortran.o  plotter.o
!# here is the output file
plotter

!combine two excutable files (my_lib.o,linsp.o)  into one (linxp)
ifort my_lib.o linsp.o -o linsp




!### output formatting 

! set the format label 100, an integer occupys 3 blocks long for the first column (right justifier[always start from the right position of this column]), 5 spaces in between, 5-digit total, 2 decimal accuracy

  100 format (i3, 5x, f5.2)
! create a file,with a reference number equals to 1.  
  open(unit=1, file='frets.dat')

  do fret=1, total_frets
    ! write to file '1', with format '100'
    write(unit=1,fmt=100) fret, scale_length/(fconst**fret)
  end do 

  close(unit=1)

! write to file without defining format 
      open(unit=1, file='data.dat')
      do i = 1,size(x)
        ! space deliminator here
        write(1,*) x(i),' ',y(i)
      end do
end program common_fortran


!!###### make a module using subroutine 
! name of the file: 
vi gnuplot_fortran.f90 

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






