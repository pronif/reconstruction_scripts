DATASET_PATH=/home/v4rl/reconstruction/Styrac_Colmap/

echo Extract features
now=$(date +"%T")
echo "Current time : $now"

colmap feature_extractor \
   --database_path $DATASET_PATH/database.db \
   --image_path $DATASET_PATH/images \
   --SiftExtraction.use_gpu 0

echo Match images
now=$(date +"%T")
echo "Current time : $now"

colmap exhaustive_matcher \
   --database_path $DATASET_PATH/database.db \
   --SIFTMatching.use_gpu 0 

mkdir $DATASET_PATH/sparse

echo Generate sparse reconstruction
now=$(date +"%T")
echo "Current time : $now"

colmap mapper \
    --database_path $DATASET_PATH/database.db \
    --image_path $DATASET_PATH/images \
    --export_path $DATASET_PATH/sparse

now=$(date +"%T")
echo "Current time : $now"

colmap model_converter --input_path $DATASET_PATH/sparse/0 --output_path $DATASET_PATH/model.nvm --output_type NVM
