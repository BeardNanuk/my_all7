program cree_carte_vp 

  implicit none


  ! to write seismograms in single precision SEP and double precision
  ! binary

  ! local parameters
  integer :: i,j,ispec,nspec, nombre_cercles,n, n_cercles, i_cercle
  real, dimension (:,:), allocatable :: position_cercle
  real, dimension (:), allocatable :: valeur_vp
  real:: x, z,longueur_cote,ecart,x_cercle, z_cercle, rayon
  logical :: dans_un_cercle
  real, dimension(:,:,:), allocatable :: x_store,z_store,vp_store
  integer,parameter :: seed = 86456
  call srand(seed)

  n=1
  nspec=900*900
  n_cercles=5000
  longueur_cote=0.0256
  ecart=0.07


  ! On remplit ce tableau avec x,z et le rayon de cercle
  allocate(position_cercle(3,n_cercles))
  allocate(valeur_vp(n_cercles))
  allocate(x_store(5,5,nspec))
  allocate(z_store(5,5,nspec))
  allocate(vp_store(5,5,nspec))

  do i=1,n_cercles
    position_cercle(1,i)=longueur_cote*3/2+(rand()-0.5)*0.02
    position_cercle(2,i)=longueur_cote*3/2+(rand()-0.5)*0.02
    position_cercle(3,i)=rand()*ecart*longueur_cote/3
    valeur_vp(i)=1500+10*(rand()-0.5)
  enddo

  open(unit=13,file='proc000000_x.bin',status='old',form='unformatted')
  open(unit=14,file='proc000000_z.bin',status='old',form='unformatted')
  open(unit=154,file='proc000000_vp.bin',status='unknown',form='unformatted')

  read(13) x_store
  read(14) z_store
  close(13)
  close(14)



  do ispec=1,nspec
    do j=1,5
      do i=1,5

      x = x_store(i,j,ispec)
      z = z_store(i,j,ispec)
      dans_un_cercle = .false.
      n=0

      do i_cercle= 1,n_cercles

        if (dans_un_cercle) cycle
        x_cercle = position_cercle(1,i_cercle)
        z_cercle = position_cercle(2,i_cercle)
        rayon = position_cercle(3,i_cercle)
        if ( (x_cercle-x)*(x_cercle-x) + (z_cercle-z)*(z_cercle-z) < rayon*rayon ) then
          dans_un_cercle=.true.
        endif
        n=n+1
      enddo
      
      if (dans_un_cercle) then
        vp_store(i,j,ispec)=valeur_vp(n)
      else
        vp_store(i,j,ispec)=1500
      endif    
      enddo
    enddo
  enddo


  write(154) vp_store
  close(154)
end  program cree_carte_vp
