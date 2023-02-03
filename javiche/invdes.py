# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/03_test_inverse_design.ipynb.

# %% auto 0
__all__ = ['insert_mode', 'plot_real', 'plot_abs']

# %% ../nbs/03_test_inverse_design.ipynb 4
import numpy as np
import matplotlib.pylab as plt
import ceviche

""" 
Patching Ceviche
"""

def insert_mode(omega, dx, x, y, epsr, target=None, npml=0, m=1, filtering=False):
    """Solve for the modes in a cross section of epsr at the location defined by 'x' and 'y'
    The mode is inserted into the 'target' array if it is suppled, if the target array is not
    supplied, then a target array is created with the same shape as epsr, and the mode is
    inserted into it.
    """
    if target is None:
        target = np.zeros(epsr.shape, dtype=complex)

    epsr_cross = epsr[x, y]
    _, mode_field = ceviche.modes.get_modes(epsr_cross, omega, dx, npml, m=m, filtering=filtering)
    target[x, y] = np.atleast_2d(mode_field)[:,m-1].squeeze()

    return target

ceviche.modes.insert_mode = insert_mode


def plot_real(val, outline=None, ax=None, cbar=False, cmap='RdBu', outline_alpha=0.5):
    """Plots the real part of 'val', optionally overlaying an outline of 'outline'
    """

    if ax is None:
        fig, ax = plt.subplots(1, 1, constrained_layout=True)
    
    vmax = np.abs(val).max()
    h = ax.imshow(np.real(val.T), cmap=cmap, origin='lower', vmin=-vmax, vmax=vmax)
    
    if outline is not None:
        ax.contour(outline.T, 0, colors='k', alpha=outline_alpha)
    
    ax.set_ylabel('y')
    ax.set_xlabel('x')
    if cbar:
        plt.colorbar(h, ax=ax)
    
    return ax

ceviche.viz.real = plot_real

def plot_abs(val, outline=None, ax=None, cbar=False, cmap='magma', outline_alpha=0.5, outline_val=None):
    """Plots the absolute value of 'val', optionally overlaying an outline of 'outline'
    """
    
    if ax is None:
        fig, ax = plt.subplots(1, 1, constrained_layout=True)      
    
    vmax = np.abs(val).max()
    h = ax.imshow(np.abs(val.T), cmap=cmap, origin='lower', vmin=0, vmax=vmax)
    
    if outline_val is None and outline is not None: outline_val = 0.5*(outline.min()+outline.max())
    if outline is not None:
        ax.contour(outline.T, [outline_val], colors='w', alpha=outline_alpha)
    
    ax.set_ylabel('y')
    ax.set_xlabel('x')
    if cbar:
        plt.colorbar(h, ax=ax)
    
    return ax

ceviche.viz.abs = plot_abs