import numpy as np
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Convert obj file to npz')
    parser.add_argument('obj_file', help='Path to obj file')
    parser.add_argument('output_file', help='Path to output npz file')
    return parser.parse_args()


def load_obj(obj_file):
    vertices = []
    faces = []
    normals = []
    texture_coords = []
    with open(obj_file, 'r') as f:
        for line in f:
            if line.startswith('v '):
                vertex = list(map(float, line.split()[1:]))
                vertices.append(vertex)
            elif line.startswith('f '):
                face = []
                for elem in line.split()[1:]:
                    if '/' in elem:
                        face_elem = list(map(int, elem.split('/')))
                    else:
                        face_elem = int(elem)
                    face.append(face_elem)
                faces.append(face)
            elif line.startswith('vn '):
                normal = list(map(float, line.split()[1:]))
                normals.append(normal)
            elif line.startswith('vt '):
                texture_coord = list(map(float, line.split()[1:]))
                texture_coords.append(texture_coord)
    return np.array(vertices, dtype=np.float32), np.array(faces),\
        np.array(normals, dtype=np.float32), np.array(texture_coords, dtype=np.float32)


def main():
    args = parse_args()
    vertices, faces, normals, texture_coords = load_obj(args.obj_file)
    np.savez_compressed(args.output_file, vertices=vertices, faces=faces, normals=normals, texture_coords=texture_coords)


if __name__ == '__main__':
    main()
