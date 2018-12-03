program cree_carte_vp 

  implicit none


  ! to write seismograms in single precision SEP and double precision
  ! binary

  ! local parameters
  integer :: i,j,ispec,nspec, nombre_cercles,n, n_cercles, i_cercle
  real, dimension (:,:), allocatable :: position_cercle
  real, dimension (:), allocatable :: valeur_vp
  real:: x, z, x_cercle, z_cercle, rayon, ecart, longueur_cote
  logical :: dans_un_cercle
  real, dimension(:,:,:), allocatable :: x_store,z_store,vp_store
  integer,parameter :: seed = 86456
  
  call srand(seed)
  n=1
  nspec=80*80
  n_cercles=350
  longueur_cote=0.0256
  ecart=0.2


  ! On remplit ce tableau avec x,z et le rayon de cercle
  allocate(position_cercle(3,n_cercles))
  allocate(valeur_vp(n_cercles))
  allocate(x_store(5,5,nspec))
  allocate(z_store(5,5,nspec))
  allocate(vp_store(5,5,nspec))

  do i=1,n_cercles
    position_cercle(1,i)= ecart*longueur_cote + longueur_cote*(1-2*ecart)*rand()
    position_cercle(2,i)= ecart*longueur_cote + longueur_cote*(1-2*ecart)*rand()
    position_cercle(3,i)= rand()*ecart*ecart*longueur_cote
    valeur_vp(i)=1500+50*(rand()-0.5)

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


      do i_cercle= 1, n_cercles

        if (dans_un_cercle) cycle
        x_cercle = position_cercle(1,i_cercle)
        z_cercle = position_cercle(2,i_cercle)
        rayon = position_cercle(3,i_cercle)
        if ( (x_cercle-x)*(x_cercle-x) + (z_cercle-z)*(z_cercle-z) < rayon*rayon ) then
          dans_un_cercle=.true.
           vp_store(i,j,ispec)= valeur_vp(i_cercle)
        endif
      enddo
      
      if (.not. dans_un_cercle) vp_store(i,j,ispec)= 1500

      n=n+1
      enddo
    enddo
  enddo


  write(154) vp_store
  close(154)
end  program cree_carte_vp
