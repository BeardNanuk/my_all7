#!/usr/bin/env python


## the actual source inversion program 

## created on Fri Nov  9 16:25:17 UTC 2018
## created by Jiaze He 

## revised on Fri Nov  9 16:49:50 UTC 2018
## trace_number range from 1 to 2. 

from scipy import interpolate

yf_stf_inverted_stack = np.zeros(1, dtype=np.complex)
for trace_num in range(inv_trace_num_star,inv_trace_num_end,1):
    execfile('ptraceprepare.py')
    # Now we change into the frequency domain

    yf_NewNormobs = yf_Newobs/(max(yf_Newobs))
    yf_NewNormsyn = yf_Newsyn/(max(yf_Newsyn))

    #yf_obs_maxnormed = yf_obs/max(yf_obs)

    # normalized received signals in the frequency domain, for plotting purposes
    yf_Newsyn_filteredsyn = yf_Newsyn*syn_taper
    yf_Newsyn_filteredNormsyn = yf_Newsyn_filteredsyn/max(yf_Newsyn_filteredsyn)

    yf_Newsyn_filteredobs = yf_Newobs*syn_taper
    yf_Newsyn_filteredNormobs = yf_Newsyn_filteredobs/max(yf_Newsyn_filteredobs)

    
    # Now we invert for the source in the frequency domain (obs as gaussian for Greens'function )
    yf_stf_inverted = np.array([0.0+0.0j])
    for i in range(1, nfftNewsyn):
        if np.abs(yf_Newsyn_filteredsyn[i]) != 0:
            #yf_stf_inverted = np.append(yf_stf_inverted, (yf_Newsyn_filteredNormsyn[i].T*yf_Newobs[i].conj().T)/(yf_Newsyn_filteredNormsyn[i].T*yf_Newsyn_filteredNormsyn[i].conj().T))
            yf_stf_inverted = np.append(yf_stf_inverted, (yf_Newsyn_filteredsyn[i].T*yf_Newobs[i].conj().T)/(yf_Newsyn_filteredsyn[i].T*yf_Newsyn_filteredsyn[i].conj().T))
        else:
            yf_stf_inverted = np.append(yf_stf_inverted, 0.0+0.0j)
    yf_stf_inverted = yf_stf_inverted.conj().T
    #yf_stf_inverted = fft(stf_inverted[0:Nt], axis=0, n=nfft)
    yf_stf_inverted_stack = yf_stf_inverted_stack + yf_stf_inverted
    stf_inverted=ifft(yf_stf_inverted,n=nfftNewsyn)
    stf_inverted_stack=ifft(yf_stf_inverted_stack,n=nfftNewsyn)


#execfile('pstf_inverse_plot.py')
