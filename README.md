# TSVI
Tutorials and codes for TSVI calculation from wall shear stress (WSS) data

The topological shear variation index (TSVI) measures the variability of the local contraction/expansion action exerted on the endothelium by the WSS along the cardiac cycle. 
It is defined as the root mean square deviation of the divergence of the normalized WSS with respect to its average over the cardiac cycle:


$$TSVI=\sqrt{\frac{1}{T}\int\limits_0^T \left[DIV_{WSS}-\overline{DIV_{WSS}}\right]^2 dt}$$
where 
$T$ is the cardiac cycle, $DIV_{WSS}$ is the divergence of the normalized WSS vector field, and $\overline{DIV_{WSS}}$ is its average over the cardiac cycle. Thus, TSVI is an integral measure of the local unsteady nature of the WSS manifolds along the cardiac cycle, and hence of the heterogeneous action of the hemodynamic forces to which endothelial cells may be focally exposed.<br />
<br />
A Python code processessing wall shear stress (WSS) data related to a surface mesh in Visualization Toolkit Polygonal (vtp) format, to calculate Topological Shear Variation Index (TSVI)
Methods for WSS analysis and visualization are explained in a tutorial video showing how TSVI can be obtained from CFD-derived WSS data in the open-source Paraview environment.<br />
<br />
*References:* <br />
1. *Mazzi V, Gallo D, Calò K, Najafi M, Khan MO, De Nisco G, Steinman DA, Morbiducci U. A Eulerian method to analyze wall shear stress fixed points and manifolds in cardiovascular flows. Biomech Model Mechanobiol. 2020 Oct;19(5):1403-1423. doi: 10.1007/s10237-019-01278-3. Epub 2019 Dec 21. PMID: 31865482.* <br />
2. *De Nisco G, Tasso P, Calò K, Mazzi V, Gallo D, Condemi F, Farzaneh S, Avril S, Morbiducci U. Deciphering ascending thoracic aortic aneurysm hemodynamics in relation to biomechanical properties. Med Eng Phys. 2020 Aug;82:119-129. doi: 10.1016/j.medengphy.2020.07.003. Epub 2020 Jul 12. PMID: 32709262.* <br />
3. *Morbiducci U, Mazzi V, Domanin M, De Nisco G, Vergara C, Steinman DA, Gallo D. Wall Shear Stress Topological Skeleton Independently Predicts Long-Term Restenosis After Carotid Bifurcation Endarterectomy. Ann Biomed Eng. 2020 Dec;48(12):2936-2949. doi: 10.1007/s10439-020-02607-9. Epub 2020 Sep 14. PMID: 32929560; PMCID: PMC7723943.*<br />
4. *Mazzi V, De Nisco G, Hoogendoorn A, Calò K, Chiastra C, Gallo D, Steinman DA, Wentzel JJ, Morbiducci U. Early Atherosclerotic Changes in Coronary Arteries are Associated with Endothelium Shear Stress Contraction/Expansion Variability. Ann Biomed Eng. 2021 Sep;49(9):2606-2621. doi: 10.1007/s10439-021-02829-5. PMID: 34324092; PMCID: PMC8455396.*
