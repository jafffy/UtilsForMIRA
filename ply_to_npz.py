import numpy as np
import argparse
import plyfile


def parse_args():
    parser = argparse.ArgumentParser(description='Convert PLY file to npz')
    parser.add_argument('ply_file', help='Path to PLY file')
    parser.add_argument('output_file', help='Path to output npz file')
    return parser.parse_args()


def load_ply(ply_file):
    with plyfile.PlyData.read(ply_file) as ply:
        vertices = np.vstack([ply['vertex']['x'], ply['vertex']['y'], ply['vertex']['z']]).T
        faces = ply['face']['vertex_indices']
        normals = None
        if 'nx' in ply['vertex'].dtype.names:
            normals = np.vstack([ply['vertex']['nx'], ply['vertex']['ny'], ply['vertex']['nz']]).T
        texture_coords = None
        if 'texture_u' in ply['vertex'].dtype.names:
            texture_coords = np.vstack([ply['vertex']['texture_u'], ply['vertex']['texture_v']]).T
    return vertices, faces, normals, texture_coords


def main():
    args = parse_args()
    vertices, faces, normals, texture_coords = load_ply(args.ply_file)
    np.savez_compressed(args.output_file, vertices=vertices, faces=faces, normals=normals, texture_coords=texture_coords)


if __name__ == '__main__':
    main()
