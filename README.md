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

**1)** Open the Script from the terminal with **Python 3.** example: **"python3 Blender\ PBR\ to\ HDRP.py"** 
![Example](https://raw.githubusercontent.com/Dante-Leoncini/PBR_Convert_toUnity/main/Documentacion/doc1.png)

You will see the following window.
![Example](https://raw.githubusercontent.com/Dante-Leoncini/PBR_Convert_toUnity/main/Documentacion/doc2.png)

**2)** **Drag** any of your textures to the window. You don't need to have them all. Automatically the program will show how many **textures it found** and their **name.** If everything is correct, click on **"crear maskMap"**
![Example](https://raw.githubusercontent.com/Dante-Leoncini/PBR_Convert_toUnity/main/Documentacion/doc3.png)

If everything went well, the **MaskMap** texture will appear in the **PNG** format
![Example](https://raw.githubusercontent.com/Dante-Leoncini/PBR_Convert_toUnity/main/Documentacion/doc4.png)

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

**1)** Abra el Script desde la terminal con **Python 3.** ejemplo: **"python3 Blender\ PBR\ to\ HDRP.py"** 
![Example](https://raw.githubusercontent.com/Dante-Leoncini/PBR_Convert_toUnity/main/Documentacion/doc1.png)

Vera la siguiente ventana:
![Example](https://raw.githubusercontent.com/Dante-Leoncini/PBR_Convert_toUnity/main/Documentacion/doc2.png)

**2)** **Arrastre** cualquiera de sus texturas a la ventana. No hace falta tenerlas todas. Automaticamente el programa mostrara cuantas **texturas encontro** y su **nombre.** Si todo es correcto haga click en **"crear maskMap"**
![Example](https://raw.githubusercontent.com/Dante-Leoncini/PBR_Convert_toUnity/main/Documentacion/doc3.png)

Si todo salio bien, aparecera en la carpeta la textura **MaskMap** en formato **PNG**
![Example](https://raw.githubusercontent.com/Dante-Leoncini/PBR_Convert_toUnity/main/Documentacion/doc4.png)

El Script no esta terminado y puede faltarle pulir un poco mas
