{ pkgs ? import <nixpkgs> {} }:

pkgs.stdenv.mkDerivation {
  name = "sandbox-julia";

  buildInputs = with pkgs; [
    python3
    python310Packages.matplotlib
    python310Packages.networkx
    python310Packages.scikit-learn
    python310Packages.numpy
    #python310Packages.scipy
    #python310Packages.jupyterlab
    #python310Packages.pip
    
  ];
  shellHook = ''
    # Make sure the GR package is installed in the current project
    julia -e 'using Pkg; Pkg.activate("./"); Pkg.add("GR")'

  # Patch the GKS binary for GR
     sudo patchelf \
     --set-interpreter ${with pkgs; pkgs.glibc}/lib/ld-linux-x86-64.so.2 \
     --set-rpath "${with pkgs; lib.makeLibraryPath [
    qt4
    gcc9 
    stdenv.cc.cc.lib
  ]}" \
     /home/horhik/.julia/artifacts/13488323454a8a92411d5d627bb0f85b9b4c7006/bin/gksqt
    python -m pip install orgparse
'';

}

# /home/user/${julia}/packages/GR/cRdXQ/deps/gr/bin/gksqt
