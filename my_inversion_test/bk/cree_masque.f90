program cree_mask

  implicit none

  ! local parameters
  integer :: i,j,ispec,iproc,nspec,NGLL,NPROC 
  real, dimension (:,:), allocatable :: position_cercle
  real:: x, z, tol, amax,size_layer
  real, dimension(:,:,:), allocatable :: x_store,z_store,vp_store
  character(len=200) :: filename
  nspec=80*80/1
  tol = 0.06
  amax=0.0256
  size_layer = tol*amax
  NGLL=5
  NPROC=1
  ! On remplit ce tableau avec x,z
  allocate(x_store(NGLL,NGLL,nspec))
  allocate(z_store(NGLL,NGLL,nspec))
  allocate(vp_store(NGLL,NGLL,nspec))


  do iproc=1,NPROC
 
  write(filename,'(a,i6.6,a)') './mask/proc',iproc-1,'_x.bin'
  open(unit=13,file=filename,status='old',form='unformatted')
  write(filename,'(a,i6.6,a)') './mask/proc',iproc-1,'_z.bin'
  open(unit=14,file=filename,status='old',form='unformatted')
  write(filename,'(a,i6.6,a)') './mask/proc',iproc-1,'_vp.bin'
  open(unit=154,file=filename,status='unknown',form='unformatted')


  read(13) x_store
  read(14) z_store
  close(13)
  close(14)


  do ispec=1,nspec
    do j=1,NGLL
      do i=1,NGLL
       x = x_store(i,j,ispec)
       z = z_store(i,j,ispec)
       if ( x< size_layer .or. z < size_layer .or. x > amax - size_layer .or. z > amax - size_layer ) then
        vp_store(i,j,ispec) = 0.0
       else if ( x< 2*size_layer .and. z > x .and. ((amax - x) > z) ) then
        vp_store(i,j,ispec) = sin( 3.1415926535/2 * (x - size_layer)/size_layer  )  
       else if ( z< 2*size_layer  .and. ((amax - x) > z )) then
        vp_store(i,j,ispec) = sin( 3.1415926535/2 * (z - size_layer)/size_layer  )         
       else if ( x > amax - 2*size_layer .and. z<x) then
        vp_store(i,j,ispec) = sin( 3.1415926535/2 * (amax - size_layer - x)/ size_layer  )  
       else if ( z > amax - 2*size_layer) then
        vp_store(i,j,ispec) = sin( 3.1415926535/2 * (amax - size_layer - z)/ size_layer  ) 
       else
        vp_store(i,j,ispec) = 1.0
       endif
      enddo
    enddo
  enddo

  write(154) vp_store
  close(154)

  enddo

end program cree_mask
