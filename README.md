# TSVI
Tutorials and codes for TSVI calculation from wall shear stress (WSS) data

The topological shear variation index (TSVI) measures the variability of the local contraction/expansion action exerted on the endothelium by the WSS along the cardiac cycle.
Methods for WSS analysis and visualization are explained in a tutorial video showing how TSVI can be obtained from CFD-derived WSS data in the open-source Paraview environment.

$$TSVI=\sqrt{\frac{1}{T}\int\limits_0^T \left[DIV_{WSS}-\overline{DIV_{WSS}}\right]^2 dt}$$
where 
$T$ is the cardiac cycle, $DIV_{WSS}$ is the divergence of the normalized WSS vector field, and $\overline{DIV_{WSS}}$ is its average over the cardiac cycle.

*References:*
*Mazzi V, Gallo D, Calò K, Najafi M, Khan MO, De Nisco G, Steinman DA, Morbiducci U. A Eulerian method to analyze wall shear stress fixed points and manifolds in cardiovascular flows. Biomech Model Mechanobiol. 2020 Oct;19(5):1403-1423. doi: 10.1007/s10237-019-01278-3. Epub 2019 Dec 21. PMID: 31865482.*
