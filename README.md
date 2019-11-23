# Monte_Carlo_StarFormation_BondiAccretion

### A Python Monte Carlo simulation looking into the formation of stars in an interstellar gas cloud with the 1-dimensional spherically symmetric Bondi accretion model

Stars form most likely from interstellar gas clouds that are initially in relative equilibrium, with some forces such as the thermodynamic pressure force pushing them apart, while others providing resistance to compression (e.g. magnetic forces). But if the density <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\rho" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\rho" title="\rho" /></a> of the interstellar gas becomes high enough locally, the pull of its own gravity becomes the dominant force and the region may contract to form a star. The different forces involved are generally well balanced on all spatial scales, therefore star formation processes happen at both the galactic and interstellar scale, ranging from large regions inside the galactic arms all the way down to dense clumps and clump cores within relatively small gas clouds that usually generate clusters. A typical cloud of molecular gas and dust (<a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\mu&space;m&space;-&space;mm" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\mu&space;m&space;-&space;mm" title="\mu m - mm" /></a> sized grains of, e.g., silicates, carbon and ices) of this size measures a few light years across and usually emits infrared light due to its small temperature (around 20 K).

In the regions where star formation is ongoing, the gas accumulates in different stages. When a core has formed, it often keeps accreting gas through an accretion disc. The latter does not only channel gas down to stars, but may also form self-gravitating condensations (e.g. planets), which can keep orbiting the stars long after the accretion disc has dispersed. In our own solar system, the coplanar orbits of the planets, as well as the presence of a tenuous dust disc are the direct results of the accretion disc our Sun had about 4.5 billion years ago.

This project presents a study done on star formation with the 1-dimensional spherically symmetric Bondi model. Because it is spherically symmetric, it does not allow for accretion discs or planet formation. We can, however address the growth and mass distribution of stars. The Bondi model is a solution of the hydrodynamics equations, which describe gas flows in the presence of a (proto-) star's gravity and pressure.

The aim of this project is to look into the formation of stars in an interstellar gas cloud with the 1-dimensional spherically symmetric Bondi model. By using a Monte Carlo simulation done in Python, we study Bondi accretion and generate an Initial Mass Function (IMF) that is then compared to the observed IMF from the Salpeter law.

The full project report contains all the necessary background information and details, equations, methods used, results and conclusions. The MATLAB script files contain code for the various cases considered, as detailed in their descriptions, and include an appropriate level of commenting and documentation.
