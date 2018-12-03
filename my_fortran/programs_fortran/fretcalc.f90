! Fretboard calculator
program fretcalc
  implicit none
  
  real :: fconst = 2.0**(1.0/12.0)
  real :: scale_length = 25.5 ! [inches]
  integer :: total_frets = 24
  integer :: fret

! set the format label 100, an integer occupys 3 blocks long for the
! first column, 5 spaces in between, 5-digit total, 2 decimal accuracy

  100 format (i3, 5x, f5.2)
! create a file,with a reference number equals to 1.
  open(unit=1, file='frets.dat')

  do fret=1,total_frets
    ! write to file '1', with format '100'
    write(unit=1, fmt=100) fret, scale_length/(fconst**fret)
  end do

  close(unit=1)

end program fretcalc
