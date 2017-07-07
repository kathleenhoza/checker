#!/usr/bin/env python3.6

import sys
import csv
import glob
import os


def main():
	
	#open a csv file containing image ids and which eyes were used to take images for each id.
	#read image ids and eyes used into lists.
	
	image_list=[]
	eye_list=[]
	
	if '.csv' in sys.argv[1]:
		f=open(sys.argv[1],'rb')
		reader = csv.reader(f)
		rownum=0
		for row in reader:
			if rownum==0:
				image_list=row
			elif rownum==1:
				eye_list=row
			rownum=rownum+1
	else:
		image_list.append(sys.argv[1])
		eye_list.append(sys.argv[2])
		
	if len(eye_list)!=len(image_list):
		print('list of eyes used is different length than number of images')
	
		return None
	
	#we'll populate this later with whatever is missing. It should really be a dictionary not a list.
	missing_data=list()

	
	for i in range(len(image_list)):

		
		working_directory = ''
		if os.path.isdir('/Volumes/RiceData'):
			working_directory='/Volumes/RiceData/MarsGroup/Mastcam/'+image_list[i]+'/working/'
		else:
			working_directory='/run/user/1000/gvfs/smb-share:server=ion.physics.wwu.edu,share=ricedata/MarsGroup/Mastcam/'+image_list[i]+'/working/'
		print(image_list[i])
		
		#***************************************************************
		#SPECTRA, ROIS
		try:
			path=working_directory+image_list[i]+'_ROIs.sel'
			rois=open(path)
			print('	'+image_list[i]+'_ROIs.sel')
		except:
			missing_data.append(image_list[i]+'_ROIs.sel')
		try:
			path=working_directory+image_list[i]+'_spectra.csv'
			spectra=open(path)
			print('	'+image_list[i]+'_spectra.csv')
		except:
			missing_data.append(image_list[i]+'_spectra.csv')
		try:
			path=working_directory+image_list[i]+'_spectra_plot.png'
			spectra=open(path)
			print('	'+image_list[i]+'_spectra_plot.png')
		except:
			missing_data.append(image_list[i]+'_spectra_plot.png')
		if 'R' in eye_list[i] and 'L' in eye_list[i]:
			try:
				path=working_directory+image_list[i]+'_avg_spectra_plot.png'
				spectra=open(path)
				print('	'+image_list[i]+'_avg_spectra_plot.png')
			except:
				missing_data.append(image_list[i]+'_avg_spectra_plot.png')
			try:
				path=working_directory+image_list[i]+'_avg_spectra.csv'
				spectra=open(path)
				print('	'+image_list[i]+'_avg_spectra.csv')
			except:
				missing_data.append(image_list[i]+'_avg_spectra.csv')
		#***************************************************************
		#RIGHT EYE DCS, FALSE COLOR, ROI IMAGE
		if 'R' in eye_list[i]:
			try:
				path=working_directory+image_list[i]+'_R*_DCS.jpg'
				DCS_R=glob.glob(path)[0]
				print('	'+DCS_R[-30:])	
			except:
				missing_data.append(image_list[i]+'_RXXX_DCS.jpg')
			try:
				path=working_directory+image_list[i]+'_R*_FalseColor.jpg'
				false_color_R=glob.glob(path)[0]
				print('	'+false_color_R[-37:])	
			except:
				missing_data.append(image_list[i]+'_RXXX_FalseColor.jpg')
			try:
				path=working_directory+image_list[i]+'_R*_ROIsOverlay.jpg'
				overlay_R=glob.glob(path)[0]
				print('	'+overlay_R[-38:])	
			except:
				missing_data.append(image_list[i]+'_RXXX_ROIsOverlay.jpg')
		#***************************************************************
		#LEFT EYE DCS, FALSE COLOR, ROI IMAGE
		if 'L' in eye_list[i]:
			try:
				path=working_directory+image_list[i]+'_L*_DCS.jpg'
				DCS_L=glob.glob(path)[0]
				print('	'+DCS_L[-30:])	
			except:
				missing_data.append(image_list[i]+'_LXXX_DCS.jpg')
			try:
				path=working_directory+image_list[i]+'_L*_FalseColor.jpg'

				false_color_L=glob.glob(path)[0]
				print('	'+false_color_L[-37:])	
			except:
				missing_data.append(image_list[i]+'_LXXX_FalseColor.jpg')
			try:
				path=working_directory+image_list[i]+'_L*_ROIsOverlay.jpg'
				overlay_L=glob.glob(path)[0]
				print('	'+overlay_L[-38:])	
			except:
				missing_data.append(image_list[i]+'_LXXX_ROIsOverlay.jpg')
				
		#***************************************************************
		#2 RIGHT EYE IMAGES
		if 'RR' in eye_list[i]:
			try:
				path=working_directory+'DCS_R2.tif'
				DCS_R=open(path)
				print('	DCS_R2')
			except:
				missing_data.append(image_list[i]+'/DCS_R2.tif')
			try:
				path=working_directory+'false_color_R2.tif'
				DCS_R=open(path)
				print('	false_color_R2')
			except:
				missing_data.append(image_list[i]+'/DCS_R2.tif')
			try:
				path=working_directory+'rois2.sel'
				rois2=open(path)
				print('	rois2')
			except:
				missing_data.append(image_list[i]+'/rois2.sel')
			try:
				path=working_directory+'rois2.sel'
				rois=open(path)
				print('	ROIs')
			except:
				missing_data.append(image_list[i]+'/rois2.sel')
			try:
				path=working_directory+'spectra2.csv'
				rois=open(path)
				print('	spectra2.csv')
			except:
				missing_data.append(image_list[i]+'/spectra2.csv')
			try:
				path=working_directory+'rois_image_R2.tif'
				rois=open(path)
				print('	rois_image_R2.tif')
			except:
				missing_data.append(image_list[i]+'/rois_image_R2.tif')

				
	print('*************************************')
	print('Missing data:')
	for missing in missing_data:
		print(missing)

		

	

if __name__ == "__main__":
    main()