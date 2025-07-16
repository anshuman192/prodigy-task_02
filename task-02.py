from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    image_array = np.array(image)
    
    # XOR operation on all pixel values
    encrypted_array = image_array ^ key
    
    encrypted_image = Image.fromarray(encrypted_array)
    encrypted_image.save(output_path)
    print(f"Encrypted image saved to {output_path}")

def decrypt_image(input_path, output_path, key):
    # XOR again with same key to decrypt
    encrypt_image(input_path, output_path, key)

def main():
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    choice = input("Enter your choice (1/2): ")

    input_path = input("Enter input image path: ")
    output_path = input("Enter output image path: ")
    key = int(input("Enter encryption/decryption key (0-255): "))

    if choice == '1':
        encrypt_image(input_path, output_path, key)
    elif choice == '2':
        decrypt_image(input_path, output_path, key)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()


