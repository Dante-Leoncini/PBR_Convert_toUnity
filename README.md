# Ingles: PBR Convert to Unity
Merge the textures into a single one ready to use in **Unity HDRP**. (Metallic, Occlusion, Detail Mask and Smoothness).
It is intended to convert textures baked with the addon **"oscurart_bake_pbr_maps"** in **Blender** link: https://github.com/oscurart/BlenderAddons

However, it can work with any texture in **EXR** format and ending with the following names:
| Texture        | nomenclature           | Example                |
|:---------------|:----------------------:|:----------------------:|
| **Occlusion**  | NAME + _AO.exr         | **NAME_AO.exr**        |
| **Metallic**   | NAME + _Metallic.exr   | **NAME_Metallic.exr**  |
| **Smoothness** | NAME + _Roughness.exr  | **NAME_Roughness.exr** |

The goal is to get the texture **"Name_MaskMap.png"**

![Example](https://raw.githubusercontent.com/Dante-Leoncini/PBR_Convert_toUnity/main/Documentacion/unity_example.jpeg)

**Note:** in order to use the script, you need to have **python-opencv** installed
In **Ubuntu** it is installed with the following command: **sudo apt install python-opencv**

The Script is not finished and may need to polish a little more

# Español: PBR Conversor para Unity
Combina las texturas en una sola, lista para usar en **Unity HDRP**. (Metallic, Occlusion, Detail Mask y Smoothness).
Esta pensado para convertir las texturas horneadas con el addon **"oscurart_bake_pbr_maps"** en **Blender** link: https://github.com/oscurart/BlenderAddons 

Sin embargo, puede funcionar con cualquier textura en formato **EXR** y que terminen con los siguientes nombres:
| Textura        | nomenclatura    | Ejemplo         |
|:---------------|:---------------:|:---------------:|
| **Occlusion**  | Nombre + _AO.exr  | **Nombre_AO.exr** |
| **Metallic**   | Nombre + _Metallic.exr  | **Nombre_Metallic.exr** |
| **Smoothness** | Nombre + _Roughness.exr  | **Nombre_Roughness.exr** |

El objetivo es conseguir la textura "**Nombre_MaskMap.png"**

![Example](https://raw.githubusercontent.com/Dante-Leoncini/PBR_Convert_toUnity/main/Documentacion/unity_example.jpeg)

**Nota:** para poder usar el script, se necesita tener instalado **python-opencv**
En **Ubuntu** se instala con el siguiente comando: **sudo apt install python-opencv**

El Script no esta terminado y puede faltarle pulir un poco mas
