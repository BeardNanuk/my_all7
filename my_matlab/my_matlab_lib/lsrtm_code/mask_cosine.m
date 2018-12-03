%% mask_cosine

function [mf_one_ring] = mask_cosine(parafilename)

eval(['load ' parafilename ' sm pl dm as s s1 indexs indexs1 rect_array_x rect_array_y']);


dx=sm.dx; % unit: m

dy=sm.dx; % unit: m

n =sm.n;
nx = sm.nx;
ny = sm.ny;

xend=dx*n;
yend=dy*n;

x_star=sm.x_star;
x_end=sm.x_end;
y_star=sm.y_star;
y_end=sm.y_end;
x_center = dm.x_center; %/% by Jiaze He    %the abscissa of simulated Damge center
y_center = dm.y_center;       % y axis of simulated Damage center


[x,y]=meshgrid(0:dx:xend,0:dy:yend);

x=x';y=y';



% array radius
radius_circle = as.ARRAY_RADIUS;
% spatial period (window width)
T_space = as.T_space;
% to adjust such that at radius = radius_circle, the total phase is 2*pi
phy = 2*pi*(1-radius_circle/T_space);

% radius inside zero
Dxy = radius_circle - T_space/2;
% radius outside zero
Dxy2 = radius_circle + T_space/2;

% % % mf_cos = 1/2*(1+cos(2*pi*sqrt((x-x_center).^2+(y-y_center).^2)/T_space));
mf_multi_rings = 1/2*(1+cos(2*pi*sqrt((x-x_center).^2+(y-y_center).^2)/T_space + phy));

mf_range1 = sqrt((x-x_center).*(x-x_center)+(y-y_center).*(y-y_center))<Dxy2+1e-12;
mf_range2 = Dxy-1e-12 < sqrt((x-x_center).*(x-x_center)+(y-y_center).*(y-y_center));

mf_one_ring = 1- mf_multi_rings.*mf_range1.*mf_range2;
% % % mf_one_ring_ones = ones(nx,ny);

