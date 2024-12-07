{
  description = "unrav's Advent of Code";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };

  outputs = { 
    self,
    nixpkgs,
    ...
  } @ inputs: let
    system = "x86_64-linux";
    pkgs = nixpkgs.legacyPackages.${system};
  in {

    devShells.${system}.default = pkgs.mkShell {
      buildInputs = let
        nixPackages = with pkgs; [
          dbus
          openssl
        ];
      in nixPackages ++ [];

      nativeBuildInputs = let
        nixPackages = with pkgs; [
          pkg-config

          cargo
          cargo-generate
          rustc
        ];
      in nixPackages ++ [];
    };

    dbus = pkgs.dbus;
  };
}
