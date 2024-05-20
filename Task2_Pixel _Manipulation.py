from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    image_array = np.array(image)
    
    # Encrypt by swapping and applying a basic operation
    encrypted_array = (image_array + key) % 256
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    image_array = np.array(image)
    
    # Decrypt by reversing the basic operation
    decrypted_array = (image_array - key) % 256
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Encrypt and decrypt images using simple pixel manipulation.")
    parser.add_argument("operation", choices=["encrypt", "decrypt"], help="Operation to perform: encrypt or decrypt")
    parser.add_argument("input_image", help="Path to the input image")
    parser.add_argument("output_image", help="Path to save the output image")
    parser.add_argument("key", type=int, help="Encryption key (integer)")

    args = parser.parse_args()

    if args.operation == "encrypt":
        encrypt_image(args.input_image, args.output_image, args.key)
    elif args.operation == "decrypt":
        decrypt_image(args.input_image, args.output_image, args.key)
