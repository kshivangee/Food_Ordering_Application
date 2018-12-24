package model;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.HashMap;
import java.util.Map;

import controller.FOS_Constants;
import javafx.collections.FXCollections;
import javafx.scene.control.cell.MapValueFactory;

public class MenuDB {
	DBConnect dbc = null;
	Connection conn;
	Statement stmt = null;
	ResultSet result = null;

	// Create table for storing Menu Details
	public void createMenuDBTable() {
		try {

			// Open a connection
			System.out.println("Connecting to database to create MenuDB Table...");
			System.out.println("Connected database successfully...");

			// Execute create query
			System.out.println("Creating MenuDB table in given database...");

			stmt = dbc.connect().createStatement();

			String sql = "CREATE TABLE "  + FOS_Constants.getMenuTableName() +  "(menu_id INTEGER NOT NULL AUTO_INCREMENT, "
					+ " item_name VARCHAR(20), " + " item_description VARCHAR(30), " + " item_price numeric(8,2), "
					+ " PRIMARY KEY(menu_id))";

			stmt.executeUpdate(sql);
			System.out.println("Created MenuDB table in given database...");
			dbc.connect().close(); // close db connection
		} catch (SQLException se) { // Handle errors for JDBC
			se.printStackTrace();
		}
	}

	public void addToFoodTable(String foodname, String fooddesc, String foodprice) throws SQLException {
		dbc = new DBConnect();
		stmt = dbc.connect().createStatement();

		String sql = "INSERT INTO " + FOS_Constants.getMenuTableName() + "(fooditem_name , food_desc ,food_price) "
				+ "VALUES (' " + foodname + " ', ' " + fooddesc + " ', ' " + foodprice + " ')";
		stmt.execute(sql);
		dbc.connect().close();
	}

	public void updateData(int foodid, String foodname, String fooddesc, String foodprice) throws SQLException {
		Connection conn = null;
		dbc = new DBConnect();

		stmt = dbc.connect().createStatement();
		String query = "Update " + FOS_Constants.getMenuTableName() + " SET fooditem_name = ' " + foodname + "' , food_desc = ' " + fooddesc
				+ " ' , food_price = ' " + foodprice + " ' WHERE fooditem_id = ' " + foodid + "'";
		stmt.executeUpdate(query);
		dbc.connect().close();
	}

	public void deleteData(int id) {
		Connection conn = null;
		dbc = new DBConnect();

		try {
			stmt = dbc.connect().createStatement();
			String sql = "DELETE FROM " + FOS_Constants.getMenuTableName() + " where fooditem_id = '" + id + "'";
			stmt.executeUpdate(sql);
			dbc.connect().close();
		} catch (SQLException e) {
			System.out.println(e);
		}
	}

	public ResultSet fetchMenuItemsFromDB() throws SQLException {
		dbc = new DBConnect();
		stmt = dbc.connect().createStatement();

		String query = "SELECT * FROM " + FOS_Constants.getMenuTableName();

		ResultSet rs = stmt.executeQuery(query);
		dbc.connect().close();

		return rs;
	}
}
