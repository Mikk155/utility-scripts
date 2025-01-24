

import os

for directory in [ "src", "utils" ]:

    for root, _, files in os.walk( directory ):

        for file in files:

            if file.endswith( ( ".cpp", ".h" ) ):

                file_path = os.path.join( root, file );

                with open( file_path, 'r', encoding='utf-8' ) as file:

                    updated_content = file.read();

                    updated_content = updated_content.replace( '\t', ' ' * 4 );

                    for typeof in [ "while", "for", "if" ]:

                        updated_content = updated_content.replace( f"{typeof} (", f"{typeof}(" );

                    updated_content = f"{updated_content}\n";

                    file.close();

                for typeof in [ "while", "for", "if" ]:

                    updated_content = updated_content.replace( f"{typeof} (", f"{typeof}(" );

                # Maybe i missed something?
                implicity_casts = [
                    "void",
                    "bool",
                    "char",
                    "signed char",
                    "unsigned char",
                    "short",
                    "unsigned short",
                    "int",
                    "unsigned int",
                    "long",
                    "unsigned long",
                    "long long",
                    "unsigned long long",
                    "float",
                    "double",
                    "long double",
                    "char*",
                    "const char*",
                    "void*",
                    "int*",
                    "float*",
                    "double*",
                    "bool*",
                    "void**",
                    "nullptr_t"
                ]

                index = 0

                while index != -1:

                    oldindex = index;

                    index = updated_content.find( "(", index + 1 );

                    if index == -1:
                        break;

                    if not updated_content[index+1:index+2] in [ ")", " " ]:

                        updated_content = updated_content[0:index+1] + " " + updated_content[index+1:]

                index = 0

                while index != -1:

                    oldindex = index;

                    index = updated_content.find( ")", index + 1 );

                    if index == -1:
                        break;

                    if not updated_content[index-1:index] in [ "(", " " ]:

                        updated_content = updated_content[0:index] + " " + updated_content[ index: ]

                for casts in implicity_casts:

                    updated_content = updated_content.replace( f"( {casts} )", f"({casts})" );

                try:

                    with open(file_path, 'w', encoding='utf-8') as file:

                        file.write( updated_content );

                except Exception as e:

                    print( f"Failed for {file_path} exception: {e}" );
